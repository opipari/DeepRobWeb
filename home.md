---
layout: page
title: Home
description: A course covering the necessary background of neural-network-based deep learning for robot perception – building on advancements in computer vision that enable robots to physically manipulate objects. ROB 498-002 and ROB 599-009 at the University of Michigan.
nav_order: 1
permalink: /
---

# DeepRob: Deep Learning for Robot Perception

ROB 498-002 & 599-009, Winter 2023 at The University of Michigan
{: .fs-6 .fw-300 }

This course covers the necessary background of neural-network-based deep learning for robot perception – building on advancements in computer vision that enable robots to physically manipulate objects. During the first part of this course, students will learn to implement, train and debug their own neural networks. During the second part of this course, students will explore recent emerging topics in deep learning for robot perception and manipulation. This exploration will include analysis of research publications in the area, building up to reproducing one of these publications for implementation as a final course project.

This course is being offered through a Distributed Teaching Collaborative between faculty at [the University of Michigan](https://umich.edu/){: target="_blank" rel="noopener noreferrer"} ([Anthony Opipari](https://topipari.com){: target="_blank" rel="noopener noreferrer"}, [Chad Jenkins](https://ocj.name/){: target="_blank" rel="noopener noreferrer"}) and [the University of Minnesota](https://twin-cities.umn.edu/){: target="_blank" rel="noopener noreferrer"} ([Karthik Desingh](https://karthikdesingh.com/){: target="_blank" rel="noopener noreferrer"}).


This course builds on and is indebted to these existing courses (as a “star” and a "fork" in the open source sense):
- [University of Michigan - EECS 498-007 / 598-005: Deep Learning for Computer Vision](https://web.eecs.umich.edu/~justincj/teaching/eecs498/WI2022/){: target="_blank" rel="noopener noreferrer"} instructed by [Justin Johnson](https://web.eecs.umich.edu/~justincj/){: target="_blank" rel="noopener noreferrer"}
- [Stanford - CS231n: Deep Learning for Computer Vision](http://cs231n.stanford.edu/index.html){: target="_blank" rel="noopener noreferrer"} instructed by [Fei-Fei Li](https://profiles.stanford.edu/fei-fei-li){: target="_blank" rel="noopener noreferrer"} and [Andrej Karpathy](https://karpathy.ai/){: target="_blank" rel="noopener noreferrer"}

---


<div class="staff-row" >
<div markdown="1" class="staff-column">

# Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

</div>
<div markdown="1" class="staff-column">

# Collaborating Instructor

{% assign instructors = site.staffers | where: 'role', 'Collaborating Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

</div>
</div>

{% assign research_associates = site.staffers | where: 'role', 'Research Associate' %}
{% assign num_research_associates = research_associates | size %}
{% if num_research_associates != 0 %}

# Research Associate

{% for staffer in research_associates %}
{{ staffer }}
{% endfor %}
{% endif %}

{% assign teaching_assistants = site.staffers | where: 'role', 'Instructional Aide' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}

# Instructional Aide

<div class="staffer-table">
{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
</div>
{% endif %}

