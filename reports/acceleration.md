---
layout: project
parent: Reports
title: Convergence Acceleration For DiffusionDet&#58;On PROPS Dataset 
description: This is a final project report for DeepRob at the University of Michigan.
authors:
  - name: Gongxing Yu
    #social: "https://topipari.com"
    affiliation: University of Michigan
  - name: Liangkun Sun
    #social: "https://xiaoxiaodu.net/"
    affiliation: University of Michigan
  - name: Yang Lyu
    affiliation: University of Michigan
  # - name: Yifu Lu
  #   affiliation: University of Michigan
  # - name: Dalton Richardson
  #   affiliation: University of Michigan
  # - name: Odest Chadwicke Jenkins
  #   social: "https://ocj.name/"
  #   affiliation: University of Michigan
---


<!-- This shows how to add an image (or gif) in markdown -->
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/our/image1.png" />
</div>


<div class="project-links" markdown="1">
[![]({{ site.baseurl }}/assets/logos/acrobat.svg){: .text-logo } Report]({{ site.baseurl }}/assets/projects/reports/our/DeepRobProjectReport.pdf){: .btn .btn-grey .mr-6 }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Code](https://github.com/fuingcrazy/DiffusionDet-on-PROPS){: .btn .btn-grey target="_blank" rel="noopener noreferrer" }
</div>


## Abstract

DiffusionDet(Diffusion based detection) is a new object detection model that learns the denoising process from ground truth boxes with gaussian noises to original gt boxes.
The authors of DiffusionDet trained and tested their model on
large dataset MS-COCO. To test and enhance DiffusionDet’s
robustness, we trained this model on a much smaller PROPS
dataset, as we observed that the convergence rate and detection
accuracy were poor, we proposed a new heatmap detection
head and introduced heatmap loss as a complement to the
model’s intrinsic loss. The result shows that the optimized model
converges much faster and outperforms the original DiffusionDet
by 1.8 AP on PROPS dataset. 

## Background Introduction
Traditional object detectors use fixed queries or predefined boxes refined via classification and regression. DiffusionDet, inspired by image denoising, introduces a “noise-to-box” approach: Gaussian noise is added to ground truth boxes during training, which are treated as ROIs on feature maps. An RNN-based decoder then learns to recover the original boxes. At inference, the model denoises random boxes to produce final detections, offering a novel method for object localization.
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/our/background.png" />
</div>

##Heatmap Head
To enhance DiffusionDet's convergence speed and improve detection performance on small or occluded objects, we propose a heatmap head as an auxiliary supervision module. The heatmap head consists of two convolution layers with a ReLU activation in between. It maps high-dimensional backbone features to class-specific heatmaps.

During training, we synthesize ground truth heatmaps using a 2D Gaussian kernel centered at each object's location:
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/our/f1.png" />
</div>
For each point (x , y) on the heatmap, we define a Gaussian response:
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/our/f2.png" />
</div>
This loss is weighted and added to the total detection loss. The heatmap serves as a spatial attention signal, allowing the model to better localize small or occluded objects. 
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/our/f3.png" />
</div>

## Results

<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/our/result.png" />
</div>
This figure provides qualitative results on sample images
from the PROPS dataset, highlighting the heatmap-enhanced
model’s capability to accurately localize objects with high
confidence, including challenging small and partially occluded
targets. The optimized DiffusionDet model enhanced by the
heatmap layer demonstrates precise localization and exception-
ally high detection confidence across various object categories.
Notably, the model achieved over 95% confidence scores for
all detected instances, illustrating the robustness and accuracy
of our proposed heatmap guidance.
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/our/result1.png" />
</div>
This figue compares the Average Precision (AP) over the course
of training. The baseline using the Swin Transformer backbone
with 30 proposals demonstrated a low initial convergence
rate. Upon transitioning to the ResNet-50 backbone with an
increased number of proposals, the AP improved considerably.
Incorporating the heatmap head led to a substantial acceler-
ation in convergence, especially evident in the early training
stages, where AP sharply rose from approximately 38% to
58% within the first 1,000 iterations. After 15,000 iterations,
the heatmap-enhanced model achieved a final AP around 67%,
surpassing the baseline approaches by approximately 10%.
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/our/resultloss.png" />
From the result we can see,when there is no Heatmap in the model,70 proposals have better result( higher APs and lower loss).After adding the Heatmap in the model,we get the highest APs and the lowest loss in shorter time.      

<!-- ## Project Video

You can display a video with your model's results by either uploading to youtube, then copying your video's `<iframe>` source as shown below. Alternatively if your video files are small, we can host them directly on the DeepRob server. -->

<!-- <div class="video-wrap">
  <div class="video-container">
	<iframe src="https://www.youtube.com/embed/dx1G7y6mhMQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
</div> -->


## Citation

If you found our work helpful, consider citing us with the following BibTeX reference:

```
@article{opipari2024deeprob,
  title = { Convergence Acceleration For DiffusionDet&:On PROPS Dataset },
  author = {Yang Lyu,Gongxing Yu,Liangkun Sun},
  year = {2025}
}
```

## Contact

If you have any questions, feel free to contact [Yang Lyu](lyuyang@umich.edu).

