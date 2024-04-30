---
layout: project
parent: Reports
title: OD-VOS&#58; Object Detection for Video Object Segmentation
description: This the website for Group 8's final project.
authors:
  - name: Omer Benharush
    affiliation: University of Michigan
  - name: Sarah Chan
    affiliation: University of Michigan
  - name: Jack Kernan
    affiliation: University of Michigan
  - name: Max Rucker
    affiliation: University of Michigan
---


<!-- This shows how to add an image (or gif) in markdown -->
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/group8/ExtensionExample2.png" width="600"/>
</div>


<div class="project-links" markdown="1">
[![]({{ site.baseurl }}/assets/logos/acrobat.svg){: .text-logo } Report]({{ site.baseurl }}/assets/projects/reports/group8/DeepRobProjectReport.pdf){: .btn .btn-grey target="_blank" rel="noopener noreferrer" }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Code](https://github.com/jrkernan/ROB498FinalProject-XMem){: .btn .btn-grey target="_blank" rel="noopener noreferrer" }
</div>


## Abstract

Long-term video object segmentation (VOS) often requires manual intervention for selecting object masks, which can be impractical for various applications in robotics. In our project, termed OD-VOS, we propose a novel approach that integrates Vision Transformer for Open-World Localization (OWL-ViT) with XMem. OWL-ViT is an object detection network that can identify objects based on text queries, and XMem is a VOS framework which efficiently stores memory inspired by the Atkinson-Shiffrin memory model. OD-VOS uses OWL-ViT to automate the mask selection process for XMem. Our method eliminates the need for manual mask selection, thus streamlining the segmentation pipeline and reducing human effort. By automating the mask selection process, our framework enhances the applicability of VOS techniques.

## Demo

Example with 1 object:

<div class="video-wrap">
  <div class="video-container">
	<iframe src="https://www.youtube.com/embed/g2ngW6zb5QY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
</div>

Example with 2 objects:

<div class="video-wrap">
  <div class="video-container">
	<iframe src="https://www.youtube.com/embed/lS44P86Mia4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
</div>

## Project Video

<div class="video-wrap">
  <div class="video-container">
	<iframe src="https://www.youtube.com/embed/cv836e0fUWA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
</div>


## Citation

If you found our work helpful, consider citing us with the following BibTeX reference:

```
@article{chan2024deeprob,
  title = {OD-VOS: Object Detection Video Object Segmentation},
  author = {Benharush, Omer and Chan, Sarah and Kernan, Jack and Rucker, Max},
  year = {2024}
}
```

## Contact

If you have any questions, feel free to contact [Sarah Chan](mailto:sjchan@umich.edu).
