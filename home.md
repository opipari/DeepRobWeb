---
layout: page
title: Home
description: A course covering the necessary background of neural-network-based deep learning for robot perception – building on advancements in computer vision that enable robots to physically manipulate objects. ROB 498-002 and ROB 599-009 at the University of Michigan.
nav_order: 1
permalink: /
---


<div class="banner-container">
<img src="{{site.baseurl}}/assets/images/banner.jpg" alt="Banner" style="width:100%;">
<div class="banner-info">
	<div class="banner-title">DeepRob</div>
	<div class="banner-subtitle">Deep Learning for Robot Perception</div>
</div>
<div class="banner-sub-info">
	<div class="banner-text">
	ROB 498-011 & 599-011
	</div>
	<div class="banner-text">
	Winter 2024 at The University of Michigan
	</div>
</div>

</div>


{: .highlight }
This website describes a course still under development. All schedules, syllabus, and plans described on this site are tentative.

This course covers the necessary background of neural-network-based deep learning for robot perception – building on advancements in computer vision that enable robots to physically manipulate objects. During the first part of this course, students will learn to implement, train and debug their own neural networks. During the second part of this course, students will explore recent emerging topics in deep learning for robot perception and manipulation. This exploration will include analysis of research publications in the area, building up to reproducing one of these publications for implementation as a final course project.

This course is being offered at [the University of Michigan](https://umich.edu/){: target="_blank" rel="noopener noreferrer"} ([Xiaoxiao Du](https://xiaoxiaodu.net){: target="_blank" rel="noopener noreferrer"}, [Anthony Opipari](https://topipari.com){: target="_blank" rel="noopener noreferrer"}, [Chad Jenkins](https://ocj.name/){: target="_blank" rel="noopener noreferrer"}).


This course builds on and is indebted to these existing courses (as a “star” and a "fork" in the open source sense):
- [University of Michigan - ROB 498-002 / 599-009: Deep Learning for Robot Perception](/w23/){: target="_blank" rel="noopener noreferrer"} instructed by [Anthony Opipari](https://web.eecs.umich.edu/~justincj/){: target="_blank" rel="noopener noreferrer"}, [Chad Jenkins](https://ocj.name/){: target="_blank" rel="noopener noreferrer"}, and [Karthik Desingh](https://karthikdesingh.com/){: target="_blank" rel="noopener noreferrer"}
- [University of Michigan - EECS 498-007 / 598-005: Deep Learning for Computer Vision](https://web.eecs.umich.edu/~justincj/teaching/eecs498/WI2022/){: target="_blank" rel="noopener noreferrer"} instructed by [Justin Johnson](https://web.eecs.umich.edu/~justincj/){: target="_blank" rel="noopener noreferrer"}
- [Stanford - CS231n: Deep Learning for Computer Vision](http://cs231n.stanford.edu/index.html){: target="_blank" rel="noopener noreferrer"} instructed by [Fei-Fei Li](https://profiles.stanford.edu/fei-fei-li){: target="_blank" rel="noopener noreferrer"} and [Andrej Karpathy](https://karpathy.ai/){: target="_blank" rel="noopener noreferrer"}


---

<div class="staff-row" >
<div markdown="1" class="staff-column">

# Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' |sort: 'order' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

</div>
<div markdown="1" class="staff-column">

# Advising Faculty

{% assign advising_faculty = site.staffers | where: 'role', 'Advising Faculty' %}
{% assign num_advising_faculty = advising_faculty | size %}
{% if num_advising_faculty != 0 %}

{% for staffer in advising_faculty %}
{{ staffer }}
{% endfor %}
{% endif %}

</div>
</div>

