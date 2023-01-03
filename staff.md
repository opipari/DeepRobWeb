---
layout: page
title: Staff
description: A directory of the teaching staff for Deep Learning for Robot Perception at the University of Michigan.
---

# Staff

<div class="staff-row" >
<div markdown="1" class="staff-column">

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

</div>
<div markdown="1" class="staff-column">

## Collaborating Instructor

{% assign instructors = site.staffers | where: 'role', 'Collaborating Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

</div>
</div>

{% assign graduate_student_instructors = site.staffers | where: 'role', 'Graduate Student Instructor' %}
{% assign num_graduate_student_instructors = graduate_student_instructors | size %}
{% if num_graduate_student_instructors != 0 %}
## Graduate Student Instructor

{% for staffer in graduate_student_instructors %}
{{ staffer }}
{% endfor %}
{% endif %}

{% assign teaching_assistants = site.staffers | where: 'role', 'Instructional Aide' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}
## Instructional Aide

{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}
