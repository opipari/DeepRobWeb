---
layout: page
title: Home
description: A course covering the necessary background of neural-network-based deep learning for robot perception – building on advancements in computer vision that enable robots to physically manipulate objects. ROB 498-002 and ROB 599-009 at the University of Michigan.
nav_order: 1
permalink: /
---

# Deep Learning for Robot Perception

ROB 498-002 & 599-009, Winter 2023 at The University of Michigan
{: .fs-6 .fw-300 }

This website describes a course still in development to be offered in the Winter 2023 semester.
{: .text-um-blue .bg-yellow-300 .fs-4 .fw-500}

This course covers the necessary background of neural-network-based deep learning for robot perception – building on advancements in computer vision that enable robots to physically manipulate objects. During the first part of this course, students will learn to implement, train and debug their own neural networks. During the second part of this course, students will explore recent emerging topics in deep learning for robot perception and manipulation. This exploration will include analysis of research publications in the area, building up to reproducing one of these publications for implementation as a final course project.

This course is being offered through a Distributed Teaching Collaborative between faculty at [the University of Michigan](https://umich.edu/){:target="_blank"} ([Anthony Opipari](https://topipari.com){:target="_blank"}, [Chad Jenkins](https://ocj.name/){:target="_blank"}) and [the University of Minnesota](https://twin-cities.umn.edu/){:target="_blank"} ([Karthik Desingh](https://karthikdesingh.com/){:target="_blank"}).


This course builds on and is indebted to these existing courses (as a “star” and a "fork" in the open source sense):
- [University of Michigan - EECS 498-007 / 598-005: Deep Learning for Computer Vision](https://web.eecs.umich.edu/~justincj/teaching/eecs498/WI2022/schedule.html){:target="_blank"} instructed by [Justin Johnson](https://web.eecs.umich.edu/~justincj/){:target="_blank"}
- [Stanford - CS231n: Deep Learning for Computer Vision](http://cs231n.stanford.edu/index.html){:target="_blank"} instructed by [Fei-Fei Li](https://profiles.stanford.edu/fei-fei-li){:target="_blank"} and [Andrej Karpathy](https://karpathy.ai/){:target="_blank"}


<div class="staff-row" >
<div markdown="1" class="staff-column">

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

</div>
<div markdown="1" class="staff-column">

## Collaborating Instructors

{% assign instructors = site.staffers | where: 'role', 'Collaborating Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

</div>
</div>

{% assign teaching_assistants = site.staffers | where: 'role', 'Instructional Aide' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}
## Instructional Aides

<div class="staffer-table">
{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
</div>
{% endif %}
