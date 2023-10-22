---
layout: project
parent: Reports
title: <i><b>Da-TRASH</b></i>&#58; Depth-appended Tabletop Recycling Algorithm for Segmenting Havoc
description: Final project webpage for "Da-TRASH" as part of DeepRob at the University of Michigan
authors:
  - name: "Ashwin Saxena"
    social: "https://www.linkedin.com/in/ashwin-s-6aa596169/"
    affiliation: "University of Michigan"
  - name: "Andrew Scheffer"
    social: "https://schefferac2020.github.io"
    affiliation: "University of Michigan"


---


<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/w23/projects/reports/da-trash/arch.webp" />
</div>


<div class="project-links" markdown="1">
[![]({{ site.baseurl }}/assets/logos/acrobat.svg){: .text-logo } Report]({{ site.baseurl }}/assets/w23/projects/reports/da-trash/da-trash.pdf){: .btn .btn-grey .mr-6 target="_blank" rel="noopener noreferrer" }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Code](https://github.com/schefferac2020/Da-TRASH){: .btn .btn-grey target="_blank" rel="noopener noreferrer" }
</div>


## Abstract

In this work, we set out to reproduce and build upon the results presented in [Learning RGB-D Feature Embeddings for Unseen Object Instance Segmentation (Xiang et al., 2021)](https://proceedings.mlr.press/v155/xiang21a/xiang21a.pdf){: target="_blank" rel="noopener noreferrer"}. This previous work makes use of deep learning and non-photorealistic, synthetic RGB + Depth data to produce surprisingly accurate *instance segmentation masks for previously unseen objects*. In this report, our team validates the previously published results that suggested combining RGB and depth feature vectors elementwise is most effective for the task of unseen object instance segmentation (UOIS). Additionally, our team extends upon previous work by adapting the existing UOIS model such that it can perform segmentation on RGB-only images. By fusing the RGB-only input images with output from a monocular depth estimation sub-network, our proposed ***Da-TRASH*** model is able to operate in environments and on robotic platforms where depth sensors are inadequite or unavailable. Thus, this project enables unseen object instance segmentation to be applicable in a broader range of robotic use cases. The proposed *Da-TRASH* model is validated on real-world trash segmentation datasets and results demonstrate the model achieves improved segmentation accuracy over existing models when depth data is unavailable.




## Experiments

The proposed *Da-TRASH* pipeline is validated on multiple real-world datasets for both its qualitative and quantitative UOIS accuracy. First, the segmentation accuracy of *Da-TRASH* is qualitatively evaluated on examples from the [ZeroWaste dataset (Bashkirova et al., 2021)](https://arxiv.org/abs/2106.02740){: target="_blank" rel="noopener noreferrer"} as shown in the following figure:

<div class="center-image">
<img style="width:74%;" alt="Quantitative measures of Da-Trash segmentation accuracy on" src="{{ site.baseurl }}/assets/w23/projects/reports/da-trash/qualitative-1.webp" />
</div>

This result demonstrates promising performance by *Da-TRASH* for segmenting previously unseen objects from an extremely cluttered scene representative of recycling facilities. More details and examples are included in [the full text]({{ site.baseurl }}/assets/w23/projects/reports/da-trash/da-trash.pdf){: target="_blank" rel="noopener noreferrer"}.

Based on the observed qualitative segmentation results, we next set out to establish how the accuracy of *Da-TRASH* compares to an RGB-only baseline, which does not use estimated depth for producing segmentation output. To perform this comparison, the [Object Segmentation Database (Richtsfeld et al., 2012)](https://www.acin.tuwien.ac.at/en/vision-for-robotics/software-tools/osd/){: target="_blank" rel="noopener noreferrer"} was chosen as it includes segmentation labels that can be used for quantitative evaluation. Results from this comparison are included in the following table, showing *Da-TRASH* has improved accuracy according to the F1-score, over an RGB-only baseline and a depth-only baseline:

<div class="center-image">
<img style="width:65%;" alt="Quantitative measures of Da-Trash segmentation accuracy on" src="{{ site.baseurl }}/assets/w23/projects/reports/da-trash/table.ii.webp" />
</div>

Moreover, qualitative results from this Object Segmentation Dataset are included below:

<div class="center-image">
<img style="width:55%;" alt="Quantitative measures of Da-Trash segmentation accuracy on" src="{{ site.baseurl }}/assets/w23/projects/reports/da-trash/qualitative-2.webp" />
</div>

For additional details and experimental results, the reader is referred to [the full project report]({{ site.baseurl }}/assets/w23/projects/reports/da-trash/da-trash.pdf){: target="_blank" rel="noopener noreferrer"}.



## Citation

If you found our work helpful, consider citing it with the following BibTeX reference:

```
@article{saxena2023da-trash,
  title = {Da-TRASH: Depth-appended Tabletop Recycling Algorithm for Segmenting Havoc},
  author = {Saxena, Ashwin and Scheffer, Andrew},
  year = {2023}
}
```


## Contact

If you have any questions, feel free to [contact us](mailto:ashwinsa@umich.edu?cc=drewskis@umich.edu).

