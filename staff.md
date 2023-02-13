---
layout: page
title: Staff
description: A directory of the teaching staff for Deep Learning for Robot Perception at the University of Michigan.
---

# Deep Rob Course Staff

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

{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}

---

# Week 7 Schedule
{: #weekly-schedule }

{% for schedule in site.schedules %}
{{ schedule }}
{% endfor %}