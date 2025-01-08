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
   - Linear Algebra: ROB 101, MATH 214, MATH 217, or equivalent
   - Multivariable Calculus (Math 215 or equivalent)
   - Systems Programming and Algorithms: ROB 320, EECS 281, or equivalent
 - Recommended prerequisites:
   - Prior experience with the [Python programming language](https://www.python.org/){: target="_blank" rel="noopener noreferrer"} is recommended.
   - Familiarity with gradients and how to calculate them from vector calculus.
   - Familiarity with random variables and probability distributions from probability theory.
   - Familiarity with concepts from machine learning (e.g. EECS 445) will be helpful.

## Programming

This course will primarily use Python and PyTorch

## Textbook

There is no required textbook for this course, however optional readings will be suggested from the textbook, ["Deep Learning" by Ian Goodfellow and Yoshua Bengio and Aaron Courville](https://www.deeplearningbook.org){: target="_blank" rel="noopener noreferrer"}.

For additional references, consider the following textbooks:
  - "[Introduction to Robotics and Perception](https://www.roboticsbook.org/){: target="_blank" rel="noopener noreferrer"}" by Frank Dellaert and Seth Hutchinson
  - "[Robotics, Vision and Control](https://link.springer.com/book/10.1007/978-3-642-20144-8){: target="_blank" rel="noopener noreferrer"}" by Peter Corke
  - "[Computer Vision: Algorithms and Applications](http://szeliski.org/Book/){: target="_blank" rel="noopener noreferrer"}" by Richard Szeliski
  - "[Foundations of Computer Vision](https://mitpress.mit.edu/9780262048972/foundations-of-computer-vision/){: target="_blank" rel="noopener noreferrer"}" by Antonio Torralba, Phillip Isola, and William T. Freeman


## Lectures

Lectures will take place in-person. 

In-person lectures will be held on **Mondays and Wednesdays from 12:00-1:30 PM ET in room CSRB 2246**.

## Discussion Sections

Discussions will take place in-person.

In-person discussions will be held on **Tuesdays from 3:30-5:30 PM ET in room CSRB 2246**.

## Programming Projects (Individual)

You will complete 5 individual programming [projects]({{ site.baseurl }}/projects/) over the course of the semester. All projects will be implemented using Python, Pytorch and Google Colab.

## Final Project (Group)

Instead of a final exam at the end of the semester, you will complete a final project working in groups of 1 to 3 students.

The final project will entail five core deliverables: (1) a written paper review, (2) an in-class paper presentation, (3) reproducing the published results of an existing deep learning paper, (4) extending the chosen paper's methods and (5) documenting your reproduction and extension in a written report.

The objective of the final project is for you to gain experience with state of the art approaches in deep learning and a sense of how research in the area is conducted.

## Midterm Exam

There will be a midterm exam that takes place in-class during the semester.


## Grading Policy

Course grades will be determined according to the following criteria:

 - [Project 0]({{ site.baseurl }}/projects/project0/):      5%
 - [Project 1]({{ site.baseurl }}/projects/):     10%
 - [Project 2]({{ site.baseurl }}/projects/):     17%
 - [Project 3]({{ site.baseurl }}/projects/):     10%
 - [Project 4]({{ site.baseurl }}/projects/):     10%
 - Midterm Exam: 10%
 - [Final Project (group)]({{ site.baseurl }}/projects/): 23%
 - In-class Activities: 10%
 - Participation: 5%

## Assignment Turn-in and Late Submission Policy

Projects reports are due at 11:59pm ET on their corresponding due date and should be submitted electronically to the Autograder or Canvas (including a photo of the signature page), respectively. For individual student projects, **three (3)** late tokens throughout the semester (1 late token corresponds to 24 hrs late, with no penalty). After all late tokens have been used, a late penalty of 10% of the total project grade per day will be applied.

## Regrades

Requests to regrade any graded assignment or project must be submitted in writing no later than one week following the return of the assignment/exam. It is important that requests be self-contained in writing such that you can carefully enunciate any errors or issues in grading.  Well-formed and valid regrade requests will allow the course staff to properly address and correct any mistakes.


## Collaboration Policy

We will mark clearly whether an assignment is for an individual or a group. For **individual** assignments, you must submit your own assignment. For **group** assignments, each team must turn in work that is wholly their own: teams are encouraged to discuss problems, strategies, ideas, algorithms, etc. with other teams, but their write-ups (including software) must be done independently. Usually, students in the same group receive the same grades for a group project. However, if a certain person(s) did not contribute or participate as reflected in in-class participation, peer review checks and lab performance, etc., their grades will be reduced at the discretion of the instructional team based on their performance.

Members of a team are required to work together on the problems. Further, each team member is expected to understand all aspects of the team project, its implementation, and underlying concepts. Proper team planning will require, at a minimum, one in-person meeting. With each problem's solution being the product of the group, all members will be held accountable for violations of the honor code. 

All code submitted must comply with the [College of Engineering Honor Code](https://bulletin.engin.umich.edu/rules/){: target="_blank" rel="noopener noreferrer"}.

On every group-based lab assignment and project, students must include a **signed** statement below, including the following statements:

 - "I participated and contributed to team discussions on each problem, and I attest to the integrity of each solution. Our team met as a group on [DATE(S)]. "
 - “Contribution of Authors: [Team member A] did [Task XXX]; [Team members B and C] did [Task YYY]; [Team members A, B and C] did [ZZZ]. [All authors] \[gave feedback on the software development, contributed to writing the report/making the demo presentation, and approved the final version for submission.\]” (*Modify the texts in brackets according to your specific team situation and member contribution. Ideally, each member/subset of members contributed to something unique, and all authors contributed to giving feedback and writing/making the final report/demo/presentations and approving the final version for submission.)


An example of a reasonable scenario might be: "Bob was out of town when we met, but Alice and Carol were able to meet on [DATE]. Bob’s ideas were emailed to us and are reflected in our final solutions." We expect exceptions to be rare, but we understand that life can be complicated! The certification should be signed by each team member, and a scan of the certification attached to the submission.

It is not acceptable to use code or solutions from outside class (including those found online) unless the resources are specifically suggested in the assignment statement. Non-permitted materials include (but not limited to) previous years' and other course materials (regardless of whether it originated from staff, students, etc.), the textbook's solution manual, etc. The use of any external material in the completion of course assignments and projects must be explicitly cited.

## Generative AI Policy

GenAI-use: **Permitted with certain rules (see below), and with disclosure.**

Consequences for inappropriate use: Reported to school-based academic misconduct processes.

Any and all use of machines that emulate human capabilities (U-M GPT, ChatGPT, Stable Diffusion, DALLE, etc. - hereinafter referred to as “GenAI” technology in general) to perform assignments or other works in the course should be **disclosed** (this includes all graded deliverables as well as other course works and activities). You must state which part of the assignment is from GenAI. 

 - For programming assignments (Project 0 - Project 4) and midterm, it is not allowed to type in the project code template in GenAI and ask GenAI to fill in - **you must do the assignment (fill in the codes and answers) yourself**. 
 - For final projects, you may use GenAI to generating ideas, editing, translating, outlining, etc. as long as you **provide proper disclosure and acknowledge your GenAI use**, In your final report, you should specify (if any) which GenAI platform you used, which part is from GenAI results, what prompt you used, any tweaks/analysis to the results (e.g., you used GenAI to generate initial idea X but you modified Y and Z, etc. )

Our goal as a community of learners is to explore and understand how these tools may be used.

U-M Generative AI website: [https://genai.umich.edu/](https://genai.umich.edu/){: target="_blank" rel="noopener noreferrer"}


## Discussion Forum

The [Piazza](https://piazza.com/class/m4pgejar4ua2qf){: target="_blank" rel="noopener noreferrer"} discussion forum is available for discussion of course materials including lectures and projects. <b>Students are not required to participate, use or join the Piazza forum.</b>

<b>Any discussion of quizzes and verbatim code on the Piazza forum must be posted privately.</b>



## Course Policies

**Academic Integrity:** All students in the class are presumed to be decent and honorable, and all students in the class are bound by the College of Engineering Honor Code. You may not seek to gain an unfair advantage over your fellow students; you may not consult, look at, or possess the unpublished work of another without their permission; and you must appropriately acknowledge your use of another’s work. 

**Accommodations for Students with Disabilities:** If you think you need an accommodation for a disability, please let us know at your earliest convenience so that we can work with the Services for Students with Disabilities (SSD) office to help us determine appropriate academic accommodations (734-763-3000; [http://ssd.umich.edu](http://ssd.umich.edu){: target="_blank" rel="noopener noreferrer"}). Any information you provide is private and confidential and will be treated as such. 

**Diversity Statement:** All members of this class are expected to contribute to a respectful, welcoming and inclusive environment for every other member of the class. We consider this classroom to be a place where you will be treated with respect, and we welcome individuals of all ages, backgrounds, beliefs, ethnicities, genders, gender identities, gender expressions, national origins, religious affiliations, sexual orientations, ability – and other visible and nonvisible differences.

**Student Well-Being:** Students may experience stressors that can impact both their academic experience and their personal well-being. These may include academic pressure and challenges associated with relationships, mental health, alcohol or other drugs, identities, finances, etc. If you are experiencing concerns, seeking help is a courageous thing to do for yourself and those who care about you. If the source of your stressors is academic, please contact me so that we can find solutions together. For personal concerns, U-M offers many resources, some of which are listed at Resources for Student Well-being on the Well-being for U-M Students website: [https://wellbeing.studentlife.umich.edu/](https://wellbeing.studentlife.umich.edu/){: target="_blank" rel="noopener noreferrer"}.

**Family Educational Rights and Privacy Act (FERPA):** Any in person course lectures may be audio/video recorded and made available to other students in this course. Students may not record or distribute any class activity without written permission from the instructor, except as necessary as part of approved accommodations for students with disabilities. Any approved recordings may only be used for the student’s own private use. 


