---
layout: project
parent: Reports
title: Speech2Mesh&#58; Generate 3D Printable Mesh with Speech Prompts
description: This is a final project report for DeepRob at the University of Michigan.
authors:
  - name: Trushant Adeshara
    social: "http://Trushant-Adeshara-UM.github.io"
    affiliation: University of Michigan
  - name: Kajal Awasthi
    social: ""
    affiliation: University of Michigan
  - name: Pannaga Sudarshan
    social: ""
    affiliation: University of Michigan
  - name: Saket Pradhan
    social: ""
    affiliation: University of Michigan
---


<!-- This shows how to add an image (or gif) in markdown -->
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/speech2mesh/speech2mesh.gif" />
</div>


<div class="project-links" markdown="1">
[![]({{ site.baseurl }}/assets/logos/acrobat.svg){: .text-logo } Report](https://github.com/Trushant-Adeshara-UM/speech2mesh/tree/main/report){: .btn .btn-grey .mr-6 }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Code](https://github.com/Trushant-Adeshara-UM/speech2mesh){: .btn .btn-grey target="_blank" rel="noopener noreferrer" }
</div>


## Abstract

Introducing "Speech-2-Mesh": an approach which swiftly transforms speech into 3D printable meshes using advanced reconstruction models. By leveraging InstantMesh, we enable easy creation of printable objects without traditional CAD software. Comparative studies with Point-E, Point2Mesh, and CAD methods underscore our efficiency and quality. This work pioneers speech-driven 3D printing, enhancing accessibility and speed while maintaining high output standards. Powered by OpenAI's Whisper and a stable diffusion model, our system generates multi-view images, which, through InstantMesh, produce optimized meshes for printing. Embracing state-of-the-art generative models, our pipeline democratizes 3D modeling, welcoming non-technical users into the fold.


## Introduction

The fusion of 3D printing with natural language processing (NLP) has ushered in a new era of accessibility and innovation in digital fabrication. By leveraging advanced NLP and 3D modeling technologies, we're witnessing a profound shift where textual descriptions seamlessly translate into tangible objects. This convergence democratizes 3D printing, empowering both enthusiasts and professionals to realize their ideas without the barriers of traditional design software. Our project, Speech-2-Mesh, exemplifies this democratization by enabling direct transformation from spoken language to 3D printable objects, bypassing conventional design processes. Through frameworks like InstantMesh and robust speech recognition models, we aim to make 3D asset creation accessible to an even wider audience, fostering creativity and inclusivity in digital fabrication.


## Algorithmic Extension

In light of recent strides in generative AI for 3D reconstruction, our focus is on integrating speech recognition, text-to-image generation, and image-to-3D conversion. Our aim is to craft a streamlined process where users can create 3D printable objects directly from spoken descriptions, sidestepping traditional modeling software. While initially exploring InstructP2P, challenges in reproducing results led us to pivot towards InstantMesh's diffusion model-based approach, enhancing our pipeline's robustness. By coupling OpenAI's Whisper speech-to-text model with InstantMesh, we convert spoken input to textual prompts, which drive multi-view image generation. These images then undergo InstantMesh's reconstruction process, culminating in high-quality 3D meshes primed for printing. This amalgamation of cutting-edge technologies facilitates efficient and user-friendly creation of 3D printed designs from spoken ideas.


## Results
Our initial findings provided valuable insights into which types of images can generate efficient meshes. In the first case, we used a cartoon image that lacked significant depth information for the 6-view diffusion model generator. However, the second prompt produced a rendered image that delivered efficient 6-view data, resulting in a more effective mesh.

![Mesh generated using Speech-2-Mesh]({{ site.baseurl }}/assets/projects/reports/speech2mesh/result.png)


## Citation

If you found our work helpful, consider citing us with the following BibTeX reference:
```
@article{trushant2024speech2mesh,
  title = {Speech-2-Mesh: Transforming Ideas into 3D Printed Creations}
  author = {Trushant Adeshara, Pannaga Sudarshan, Kajal Awasthi, and Saket Pradhan},
  year = {2024}
}
```


## Contact

If you have any questions, feel free to contact [Trushant Adeshara, Pannaga Sudarshan, Kajal Awasthi and Saket Pradhan](mailto:trushant@umich.edu?cc=pannaga@umich.edu?cc=kajalaw@umich.edu?cc=saketp@umich.edu).

