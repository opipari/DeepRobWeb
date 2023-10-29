---
layout: page
title: Staff
description: A directory of the teaching staff for Deep Learning for Robot Perception at the University of Michigan.
---

# Deep Rob Course Staff

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

