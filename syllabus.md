---
layout: page
title: Syllabus
description: Course policies and information pertaining to Deep Learning for Robot Perception at the University of Michigan.
nav_order: 2
---

# Course Syllabus: Deep Learning for Robot Perception
{:.no_toc}


## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

{: .highlight }
**Note: This course website and syllabus is still under development and is subject to change.**

## About

Robots need to see and understand their world to be able to interact with objects and perform useful tasks autonomously. Perception is the essential first step in the process for endowing robots to perform autonomously.  Autonomous robots need to make sense of their sensory observations to represent the world around them – and enable their reasoning and action to a goal. Visual perception with cameras as sensors has matured due to the recent advancements in neural networks – which is especially true for performing visual recognition tasks such as object classification, detection, pose estimation, grasp pose detection, etc. 

This course aims to cover the necessary background of neural-network-based deep learning for robot perception – building on advancements in computer vision and enabling – for enabling robots to dexterously manipulate physical objects. During the first part of this course, students will learn to implement, train and debug their own neural networks. During the second part of this course, students will explore recent emerging topics in deep learning for robot perception and manipulation.  This exploration will include analysis of research publications in the area, building up to reproducing and implementing state-of-the-art deep learning approaches as a final course project.

This course builds on and is indebted to these existing courses (as a “star” and a "fork" in the open source sense):
- [University of Michigan - ROB 498-011 / 599-011: Deep Learning for Robot Perception](/w24/){: target="_blank" rel="noopener noreferrer"} instructed by [Xiaoxiao Du](https://xiaoxiaodu.net){: target="_blank" rel="noopener noreferrer"}, [Anthony Opipari](https://topipari.com/){: target="_blank" rel="noopener noreferrer"}, and [Chad Jenkins](https://ocj.name/){: target="_blank" rel="noopener noreferrer"}
- [University of Michigan - ROB 498-002 / 599-009: Deep Learning for Robot Perception](/w23/){: target="_blank" rel="noopener noreferrer"} instructed by [Anthony Opipari](https://topipari.com/){: target="_blank" rel="noopener noreferrer"}, [Chad Jenkins](https://ocj.name/){: target="_blank" rel="noopener noreferrer"}, and [Karthik Desingh](https://karthikdesingh.com/){: target="_blank" rel="noopener noreferrer"}
- [University of Michigan - EECS 498-007 / 598-005: Deep Learning for Computer Vision](https://web.eecs.umich.edu/~justincj/teaching/eecs498/WI2022/){: target="_blank" rel="noopener noreferrer"} instructed by [Justin Johnson](https://web.eecs.umich.edu/~justincj/){: target="_blank" rel="noopener noreferrer"}
- [Stanford - CS231n: Deep Learning for Computer Vision](http://cs231n.stanford.edu/index.html){: target="_blank" rel="noopener noreferrer"} instructed by [Fei-Fei Li](https://profiles.stanford.edu/fei-fei-li){: target="_blank" rel="noopener noreferrer"} and [Andrej Karpathy](https://karpathy.ai/){: target="_blank" rel="noopener noreferrer"}


## Topics and Course Structure

The first half of the course will cover deep learning fundamentals in computer vision catered to robot perception problems.

- Linear classifiers
- Stochastic gradient descent
- Fully-connected networks
- Convolutional networks

The second half of the course will switch to seminar style covering following advanced topics in robot perception and manipulation via discussing publications.

- 3D vision in robotics
- Pose estimation
- Object perception for robot manipulation
- Neural radiance fields for perception
- Robot grasp pose detection

## Prerequisites

 - Strongly encouraged prerequisites:
   - Programming: ROB 320, EECS 281, or equivalent
   - Linear Algebra: ROB 101, MATH 214, MATH 217, or equivalent
 - Recommended prerequisites:
   - Prior experience with the [Python programming language](https://www.python.org/){: target="_blank" rel="noopener noreferrer"} is recommended.
   - Familiarity with gradients and how to calculate them from vector calculus.
   - Familiarity with random variables and probability distributions from probability theory.
   - Familiarity with concepts from machine learning (e.g. EECS 445) will be helpful.

## Textbook

There is no required textbook for this course, however optional readings will be suggested from the textbook, ["Deep Learning" by Ian Goodfellow and Yoshua Bengio and Aaron Courville](https://www.deeplearningbook.org){: target="_blank" rel="noopener noreferrer"}.

For additional references, consider the following textbooks:
  - "[Introduction to Robotics and Perception](https://www.roboticsbook.org/){: target="_blank" rel="noopener noreferrer"}" by Frank Dellaert and Seth Hutchinson
  - "[Robotics, Vision and Control](https://link.springer.com/book/10.1007/978-3-642-20144-8){: target="_blank" rel="noopener noreferrer"}" by Peter Corke
  - "[Computer Vision: Algorithms and Applications](http://szeliski.org/Book/){: target="_blank" rel="noopener noreferrer"}" by Richard Szeliski
  - "[Foundations of Computer Vision](https://mitpress.mit.edu/9780262048972/foundations-of-computer-vision/){: target="_blank" rel="noopener noreferrer"}" by Antonio Torralba, Phillip Isola, and William T. Freeman


## Lectures

Lectures will take place in-person. 

In-person lectures will be held on **Mondays and Wednesdays from 12:00-1:30 PM EST in room CSRB 2246**. Remote access will be available through Zoom.

## Discussion Sections

Discussions will take place in-person.<!--  with remote accessibility (synchronous and asynchronous).  -->

In-person discussions will be held on **Tuesdays from 3:30-5:30 PM EST in room CSRB 2246**. Remote access will be available through Zoom.

## Programming Projects

You will complete 5 programming [projects]({{ site.baseurl }}/projects/) over the course of the semester. All projects will be implemented using Python, Pytorch and Google Colab.

## Final Project

Instead of a final exam at the end of the semester, you will complete a final project working in groups of 1 to 3 students.

The final project will entail five core deliverables: (1) a written paper review, (2) an in-class paper presentation, (3) reproducing the published results of an existing deep learning paper, (4) extending the chosen paper's methods and (5) documenting your reproduction and extension in a written report.

The objective of the final project is for you to gain experience with state of the art approaches in deep learning and a sense of how research in the area is conducted.

## Quizzes

Throughout the semester, there will be a total of 16 quizzes administered through [gradescope](https://www.gradescope.com/courses/704549){: target="_blank" rel="noopener noreferrer"}. These quizzes will be posted before lecture sections throughout the semester and be available to take until the beginning of lecture that same day. Quizzes will be released at 7:00AM EST and must be submitted by 5:00PM EST. Each quiz will have a 15 minute time limit. Each quiz will consist of 1 or 2 short questions within the scope of previously covered lectures and graded projects. Use of lecture, project and other course materials is permitted while taking the quizzes. Use of external sources (i.e. from the internet) is not permitted during quizzes. 

## Grading Policy

Course grades will be determined according to the following criteria:

 - [Project 0]({{ site.baseurl }}/projects/):      6%
 - [Project 1]({{ site.baseurl }}/projects/):     12%
 - [Project 2]({{ site.baseurl }}/projects/):     12%
 - [Project 3]({{ site.baseurl }}/projects/):     12%
 - [Project 4]({{ site.baseurl }}/projects/):     12%
 - [Final Project]({{ site.baseurl }}/projects/):
   - Paper Review: 5%
   - Paper Presentation: 10%
   - Paper Reproduction: 5%
   - Algorithmic Extension: 5%
   - Written Report: 5%

 - 16 Pre-Lecture Quizzes: 16% (1% each)

## Collaboration Policy

The free flow of discussion and ideas is encouraged. <b>However, all work submitted must be your own.</b>

All code submitted must comply with the [College of Engineering Honor Code](https://bulletin.engin.umich.edu/rules/){: target="_blank" rel="noopener noreferrer"}.

No code can be communicated, including verbally. Explicit use of external sources must be clearly cited. Experimentation with and use of generative AI as an educational tool is encouraged, however any use of AI for course work must abide by the College of Engineering Honor Code and must be clearly cited.


## Discussion Forum

The [Piazza](https://piazza.com/umich/winter2024/rob498011598012/home){: target="_blank" rel="noopener noreferrer"} discussion forum is available for discussion of course materials including lectures and projects. <b>Students are not required to participate, use or join the Piazza forum.</b>

<b>Any discussion of quizzes and verbatim code on the Piazza forum must be posted privately.</b>



