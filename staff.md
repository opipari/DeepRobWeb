---
layout: page
title: Staff
description: A directory of the teaching staff for Deep Learning for Robot Perception at the University of Michigan.
nav_order: 10
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

## Graduate Student Instructor
<div markdown="1" class="staff-column">

{% assign gsis = site.staffers | where: 'role', 'Graduate Student Instructor' |sort: 'order' %}
{% assign num_gsis = gsis | size %}
{% if num_gsis != 0 %}

{% for staffer in gsis %}
{{ staffer }}
{% endfor %}
{% endif %}

</div>

## Instructional Assistants
<div markdown="1" class="staff-column">

{% assign ias = site.staffers | where: 'role', 'Instructional Assistant' | sort: 'order' %}
{% for staffer in ias %}
{{ staffer }}
{% endfor %}

</div>

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


# Office Hours Schedule
{: #weekly-schedule }

<div markdown="1" style="max-width: 1100px">
{: .highlight }
**The schedule of instructor office hours, including the in-person locations, is provided in the following Google calendar.**
</div>

<div markdown="1" style="max-width: 1100px">
{: .note }
**For accessing office hours virtually, please refer to the calendar for each instructor's preferred Zoom link. If no Zoom link is listed, please join their office hours queue and share your personal Zoom link as your location.**
</div>

<iframe src="https://calendar.google.com/calendar/embed?src=c_0d878f9fac4a6afae0d039faeb59b0ea94ebfa0b65fbe8be4f3d7a573c97875f%40group.calendar.google.com&ctz=America%2FDetroit" style="border:solid 1px #777" width="1100" height="600" frameborder="0" scrolling="no"></iframe>
