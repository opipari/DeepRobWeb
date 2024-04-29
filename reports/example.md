---
layout: project
parent: Reports
title: GrapeRob - A Grape Localization Pipeline for Automated Robotic Harvesting
description: This is a final project report for DeepRob at the University of Michigan.
authors:
  - name: Anthony Opipari
    email: advaithb@umich.edu
    affiliation: University of Michigan
    year: 2nd Year Robotics B.S.E.
    hometown: Ann Arbor, MI
  - name: Isaac Madhavaram
    email: imadhav@umich.edu
    affiliation: University of Michigan
    year: 3rd Year Robotics B.S.E.
    hometown: Ann Arbor, MI
---


<!-- This shows how to add an image (or gif) in markdown -->
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/example/stem_masking_final.jpg" />
</div>


<div class="project-links" markdown="1">
[![]({{ site.baseurl }}/assets/logos/acrobat.svg){: .text-logo } Report](#){: .btn .btn-grey .mr-6 }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Code](https://github.com/adi-balaji/grape_juice){: .btn .btn-grey target="_blank" rel="noopener noreferrer" }
</div>


## Abstract

Grapes are a globally significant fruit utilized not only for consumption but also for wine production. However, manual grape harvesting faces challenges due to labor shortages and technical intricacies. This paper proposes a robotic grape harvesting system using deep learning based robot perception and 3D reconstruction to compute grape bunch and stem poses for robotic picking. Drawing from previous research in agricultural robotics, this system extends existing methodologies by integrating a novel stem segmentation model into the vision pipeline, and testing on a robotic platform to gauge accuracy. Experiments on the Fetch mobile manipulation shows a grasp success rate of 85.71% and an average gripper pose error of 4 cm on less than 150 training images. Authors can be contacted via email regarding questions, clarifications, and data availability. Below is our methods and results of our experiment.

## Initial Paper and Background

The core problem addressed is the need for efficient fruit detection and accurate pose estimation for the furtherment of agricultural robotics. The key idea involves utilizing Mask R-CNN for fruit segmentation and point cloud extraction for pose estimation, and the implementation involves image preprocessing, fruit segmentation, point cloud construction, and pose estimation using a RANSAC cylinder model fitting approach. The evaluation methodology includes metrics such as precision, recall, and intersection over the union (IoU) to evaluate the performance under different lighting conditions. Finally, the paper concludes that the proposed approach achieves high precision and recall rates, an average IoU of about 82\%, and a quick inference time of 1.7 seconds, demonstrating its viability for real-world application in grape harvesting robotics.

Overall, Yin et al. presents a noteworthy contribution to the field of agricultural robotics and computer vision in relation to detecting the grape poses. The relevance of the paper to the field of agricultural robotics is clear, as it offers practical solutions to enhance the efficiency and automation of agricultural farming practices. However, there are a few areas for improvement; while the paper effectively addresses the core problem and presents a novel approach, it could benefit from a more in depth evaluation of their methods. Their novel pose estimation pipeline was only evaluated on inference time, not accuracy, and does not test the implementation of such an algorithm on a physical robot - leaving the viability of the pipeline unexamined. Additionally, for a robotic implementation, the pipeline’s detection capabilities are insufficient as a robot needs stem pose in addition to bunch pose for manipulation. 

## Our Work

In our work, we address these issues in our algorithmic reproduction and extension. We adopted a Mask R-CNN model architecture for both masking branches using the PyTorch and torchvision libraries in order to infer accurate masks for precise localization. The embedded region proposal network uses the extracted feature map calculated by the ResNet FPN to propose RoIs for the mask and box predictors. A mask predictor and box predictor layer was thus added to the RoI Heads for mask and bounding box inference at the end. For testing on the Fetch Mobile Manipulation platform, the depth map directly from Fetch’s infrared sensor was more reliable. Depending on whether the robot should navigate to the bunch or stem, the pipeline will first take the segmentation mask and crop the depth map to the bunch or stem. This provides the per pixel depth of the mask that can be used for 3D reconstruction. A more detailed explanation of the process and methods can be found in the paper linked above.

## Results

Visual results are great for project webpages; exciting results can captivate an audience and convey dense information efficiently. We suggest including images, figures, animations, and videos on your webpage. For example, static images can be displayed as shown below:

![DeepRob Logo]({{ site.baseurl }}/assets/logos/favicons/UMich_favicon_dark.png)


## Project Video

You can display a video with your model's results by either uploading to youtube, then copying your video's `<iframe>` source as shown below. Alternatively if your video files are small, we can host them directly on the DeepRob server.

<div class="video-wrap">
  <div class="video-container">
	<iframe src="https://www.youtube.com/embed/dx1G7y6mhMQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
</div>


## Citation

If you found our work helpful, consider citing us with the following BibTeX reference:

```
@article{opipari2023deeprob,
  title = {Example Project: A final project template for DeepRob},
  author = {Opipari, Anthony and Zhang, Huijie and Zhu, Jiyue and Desingh, Karthik and Jenkins, Odest Chadwicke},
  year = {2023}
}
```
Be sure to update this reference to include your team's author information for correct attribution!


## Contact

If you have any questions, feel free to contact [Anthony Opipari and Prof. Chad Jenkins](mailto:topipari@umich.edu?cc=ocj@umich.edu).

