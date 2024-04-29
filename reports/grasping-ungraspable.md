---
layout: project
parent: Reports
title: Choosing how to Grasp the Ungraspable
description: This is the final project report for Group 20
authors:
  - name: Jason Brown
    affiliation: University of Michigan
  - name: Eli Fox
    affiliation: University of Michigan
  - name: Jacob Harrelson
    affiliation: University of Michigan
  - name: Srushti Hippargi
    affiliation: University of Michigan
---


<!-- This shows how to add an image (or gif) in markdown -->
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/example/deeprob.gif" />
</div>


<div class="project-links" markdown="1">
[![]({{ site.baseurl }}/assets/logos/acrobat.svg){: .text-logo } Report](#){: .btn .btn-grey .mr-6 }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Code](https://github.com/HarrelsonJ/DeepRob_Ungraspable/tree/main){: .btn .btn-grey target="_blank" rel="noopener noreferrer" }
</div>



## Abstract

TODO Abstract


## Results

The results of training for different types of occlusions are shown below. In each type of occlusion, the robot selects an appropriate policy and executes that policy to pick up the block and reach the target grasp. The policy selection uses the box's size. If the box is small enough to be picked up from the top, the bot selects the side occlusion policy. Otherwise, if the block is small enough to be picked up from the side, the bot selects the ground occlusion policy.

<div class="spread-video-wrap">
	<iframe src="https://www.youtube.com/embed/S2uZXtmPDoo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
	<iframe src="https://www.youtube.com/embed/Gy8gUC2zcEQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
	<iframe src="https://www.youtube.com/embed/zOsRI8oXJOs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

<style>
.spread-video-wrap {
    display: flex;
    justify-content: space-between;
    width: 100%;
}

.spread-video-wrap iframe {
    width: 30%;
    height: 350px;
}
</style>

We found that the policy selector was 100% effective in simulation, and when the correct policy was selected the simulated robot was able to pick up the block with a 100% success rate. Future work could include transferring ADR-trained policies to a real robot and seeing how they compare.


## Citation

If you found our work helpful, consider citing us with the following BibTeX reference:

```
@article{ungraspable2024deeprob,
  title = {Choosing how to Grasp the Ungraspable},
  author = {Brown, Jason and Fox, Eli and Harrelson, Jacob and Hippargi, Srushti},
  year = {2024}
}
```

## Contact

If you have any questions, feel free to contact [Eli Fox](mailto:elijfox@umich.edu).

