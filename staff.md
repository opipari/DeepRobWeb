---
layout: page
title: Staff
description: A directory of the teaching staff for Deep Learning for Robot Perception at the University of Michigan.
---

# Deep Rob Course Staff

---

## Instructors
<div markdown="1" class="staff-column">

{% assign instructors = site.staffers | where: 'role', 'Instructor' |sort: 'order' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

</div>

<!-- ## Graduate Student Instructor
<div markdown="1" class="staff-column">

{% assign gsis = site.staffers | where: 'role', 'Graduate Student Instructor' |sort: 'order' %}
{% assign num_gsis = gsis | size %}
{% if num_gsis != 0 %}

{% for staffer in gsis %}
{{ staffer }}
{% endfor %}
{% endif %}

</div> -->

<!-- ## Instructional Assistants
<div markdown="1" class="staff-column">

{% assign ias = site.staffers | where: 'role', 'Instructional Assistant' | sort: 'order' %}
{% for staffer in ias %}
{{ staffer }}
{% endfor %}

</div> -->

## Advising Faculty
<div markdown="1" class="staff-column">

{% assign advising_faculty = site.staffers | where: 'role', 'Advising Faculty' %}
{% assign num_advising_faculty = advising_faculty | size %}
{% if num_advising_faculty != 0 %}

{% for staffer in advising_faculty %}
{{ staffer }}
{% endfor %}
{% endif %}

</div>

