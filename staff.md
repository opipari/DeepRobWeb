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

{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}
