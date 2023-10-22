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

# Research Associate

{% assign research_associates = site.staffers | where: 'role', 'Research Associate' %}
{% assign num_research_associates = research_associates | size %}
{% if num_research_associates != 0 %}

{% for staffer in research_associates %}
{{ staffer }}
{% endfor %}
{% endif %}

</div>
</div>

