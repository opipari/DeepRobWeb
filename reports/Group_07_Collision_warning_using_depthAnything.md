---
layout: project
parent: Reports
title: Collision Avoidance using Depth Anything for Advanced Rider Assistance System (ARAS)
description: This is a final project report for DeepRob at the University of Michigan.
authors:
  - name: Zesen Zhao
    social: "https://www.linkedin.com/in/zesen-zhao-b1b859244/"
    affiliation: University of Michigan
  - name: Anup Bagali
    social: "https://www.linkedin.com/in/abagali1/"
    affiliation: University of Michigan
  - name: Kanishka Gabel
    social: "https://www.linkedin.com/in/kanishka-gabel/"
    affiliation: University of Michigan
--- 


<!-- This shows how to add an image (or gif) in markdown -->
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/Group_07_Collision_warning_using_depthAnything/Depthanything.png" />
</div>


<div class="project-links" markdown="1">
[![]({{ site.baseurl }}/assets/logos/acrobat.svg){: .text-logo } Report](https://drive.google.com/drive/folders/1vB9Y4QksGINOILUpjn0_mR9GcfMDtsS2?usp=sharing){: .btn .btn-grey .mr-6 }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Code](https://github.com/abagali1/Depth-Anything-ROB599){: .btn .btn-grey target="_blank" rel="noopener noreferrer" }
</div>


## Abstract

Depth Anything offers zero-shot ability and compact size for versatile depth estimation, ideal for edge devices. Our Collision Warning system capitalizes on its depth perception prowess, analyzing depth gradients for obstacle detection. Low-gradient areas are sky blue, while high-gradient zones signal potential obstacles in purple. Predicted paths triggering alerts upon intersection with high-gradient regions empower proactive risk identification, crucial for safe navigation. Seamlessly integrating depth estimation and collision warning, this extension enhances Depth Anything's value across robotics and autonomous systems, ensuring reliable obstacle avoidance and dynamic path planning in diverse environments.


## Method
The collision warning extension builds upon the robust depth estimation capabilities of Depth Anything to enable proactive obstacle detection and avoidance for autonomous navigation systems. The algorithm comprises the following key steps:

<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/Group_07_Collision_warning_using_depthAnything/Collision_warning.png" />
</div>

The collision warning extension enhances autonomous navigation systems by utilizing Depth Anything's depth estimation to detect obstacles. Preprocessing resizes input video for compatibility, while depth estimation generates depth maps per frame. Depth gradient computation identifies potential obstacles, visualized for clarity. Path prediction generates the system's trajectory, overlaid on the depth gradient for collision risk assessment. Alerts are triggered for potential collisions, aiding in safe navigation. This proof-of-concept integrates depth estimation, gradient analysis, path prediction, and collision risk assessment for proactive obstacle detection. Further development may include advanced path planning and sensor fusion for real-world integration.

## Results
In the figure below the output of our algorithm can be seen. It successfully detects the person who is in the predicted path of the vehicle and triggers a warning on the screen with Danger sign. This warning can be used to trigger an alarm or provide any kind of vibrational feedback to alert the driver about the danger.

<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/Group_07_Collision_warning_using_depthAnything/results.png" />
</div>


## Demo Video


<div class="video-wrap">
  <div class="video-container">
	<iframe src="https://www.youtube.com/embed/pllGkFznlS4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
</div>


## Citation

If you found our work helpful, consider citing us with the following BibTeX reference:

```
@article{2024deeprob,
  title = {Collision Avoidance using Depth Anything for Advanced Rider Assistance System (ARAS)},
  author = {Zhao, Zesen and Bagali, Anup and Gabel, Kanishka},
  year = {2024}
}
```
Be sure to update this reference to include your team's author information for correct attribution!


## Contact

If you have any questions, feel free to contact [Zesen Zhao](mailto:hymanzzs@umich.edu), [Anup Bagali](mailto:abagali@umich.edu), [Kanishka Gabel](mailto:kgabel@umich.edu).

