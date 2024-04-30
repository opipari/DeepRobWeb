---
layout: project
parent: Reports
title: Automatic Data Generation for SORNet&#58; PROPS Relation Dataset
description: This is a final project report for DeepRob at the University of Michigan.
authors:
  - name: Jace Aldrich
    social: "https://jacealdrich.com"
    affiliation: University of Michigan
  - name: Ariana Verges Alicea
    affiliation: University of Michigan
  - name: Hannah Ho
    affiliation: University of Michigan
---


<!-- This shows how to add an image (or gif) in markdown -->
<div class="center-image">
<img style="width:75%;" alt="SornetArchitecture" src="{{ site.baseurl }}/assets/projects/reports/props-relation/sornet_model.webp" />
<div>SORNet Architecture as specified by the original authors <a href="https://sites.google.com/view/sornet-extended/" target="_blank" rel="noopener noreferrer" >(Yuan et al., 2021)</a>.</div>
</div>


<div class="project-links" markdown="1">
[![]({{ site.baseurl }}/assets/logos/acrobat.svg){: .text-logo } Report]({{ site.baseurl }}/assets/projects/reports/props-relation/Sornet_Props_Report.pdf){: .btn .btn-grey .mr-6 target="_blank" rel="noopener noreferrer" }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Dataset Code](https://github.com/Jaldrich2426/PROPS-Relation-Dataset){: .btn .btn-grey .mr-6 target="_blank" rel="noopener noreferrer" }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Model Code](https://github.com/Jaldrich2426/sornet){: .btn .btn-grey target="_blank" rel="noopener noreferrer" }
</div>


## Abstract

Spatial Object-Centric Representation Network [(SORNet, Yuan et al., 2021)](https://sites.google.com/view/sornet-extended/){: target="_blank" rel="noopener noreferrer"} is a network architecture that takes an RBG image with several canonical object views and outputs object-centric embeddings. The authors of the original paper trained and tested SORnet on their custom Leonardo and Kitchen data sets, as well as the CLEVR dataset (Compositional Language and Elementary Visual Reasoning). We expanded SORnet's capability by training it on [PROPS Dataset]({{ site.baseurl }}/datasets/props-pose){: target="_blank" rel="noopener noreferrer"} (Progress Robot Object Perception Samples), which was extensively used throughout this course. Training SORNet with PROPS dataset allow us to test its capabilities to a real-world dataset in order to better understand how it performs in real-life applications.

## Introduction
There are a plethora of applications for robots that can perform sequential tasks that involve manipulating objects around them. These tasks can range from object assembly to organizing and sorting to packing to much more. However, in order to perform these tasks, robots need a way to recognize the orientation of objects in the world frame and in relation to each other. Having accurate results on the positional relationships between objects in a real-world setting is important in order to perform those tasks. So we tackled applying SORNet to real-world data through training it on the PROPS dataset.

## Algorithmic Extension
Our update to SORnet introduces an algorithmic extension designed to boost its performance with real-world data. By developing a base class to compute relations on 3D pose or bounding box datasets, we have made it possible for SORnet to process a diverse range of datasets, including scene images, identifiable objects, and 3D object coordinates. Users only need to overload a few methods to return image and object data, and their dataset will be compatable with SORNet. This enhancement notably streamlines the conversion of data into a format that SORnet can handle.
<!-- This shows how to add an image (or gif) in markdown -->
<div class="center-image">
<img style="width:75%;" alt="CanonicalViews" src="{{ site.baseurl }}/assets/projects/reports/props-relation/obj_cannonicals.webp" />
<div>PROPS Best Object Canonical Views</div>
</div>


## Results 
As an example of our dataset conversion framework, SORNet was trained on the [PROPS Pose dataset]({{ site.baseurl }}/datasets/props-pose){: target="_blank" rel="noopener noreferrer"}, with the resulting dataset named the PROPS Relation Dataset. It trained on relations regarding if objects in the dataset are "left", "right", "in front of", or "behind" other objects. 

### Example Predicate Classifications
<!-- This shows how to add an image (or gif) in markdown -->
<div class="center-image">
<img style="width:85%;" alt="BoxesResult" src="{{ site.baseurl }}/assets/projects/reports/props-relation/query_boxes.webp" />
</div>

<!-- This shows how to add an image (or gif) in markdown -->
<div class="center-image">
<img style="width:85%;" alt="CannedResult" src="{{ site.baseurl }}/assets/projects/reports/props-relation/query_cans.webp" />
</div>

### Model Performance
With the PROPS Relational dataset, SORNet achieved over 99% total validation accuracy, and over 98% validation accuracy per object, demonstrating the efficacy of our approach. These results are almost identical to that of results on n CLEVR-CoGenT.
<table border="1" style="width:100%; text-align:center; border-collapse: collapse;">
<caption style="caption-side: bottom; text-align: center;"><b>Full Size PROPS Data Validation Accuracy Percentages</b> for all Relationships. Querries are in the form of "is [<em>row</em>] [<em>relation</em>] [<em>column</em>]?", e.g., "is the potted meat can behind the master chef can?"</caption>
    <tr>
        <th>&nbsp;</th>
        <th>Master<br>Chef Can</th>
        <th>Cracker<br>Box</th>
        <th>Sugar<br>Box</th>
        <th>Tomato<br>Soup Can</th>
        <th>Mustard<br>Bottle</th>
        <th>Tuna<br>Fish Can</th>
        <th>Gelatin<br>Box</th>
        <th>Potted<br>Meat Can</th>
        <th>Mug</th>
        <th>Large<br>Marker</th>
        <th>Average</th>
    </tr>
    <tr>
        <td><b>Master Chef Can</b></td>
        <td>-</td>
        <td>99.30</td>
        <td>99.77</td>
        <td>98.80</td>
        <td>98.90</td>
        <td>98.77</td>
        <td>98.65</td>
        <td>99.20</td>
        <td>99.15</td>
        <td>98.85</td>
        <td>99.04</td>
    </tr>
    <tr>
        <td><b>Cracker Box</b></td>
        <td>99.10</td>
        <td>-</td>
        <td>99.37</td>
        <td>99.80</td>
        <td>99.20</td>
        <td>99.39</td>
        <td>98.54</td>
        <td>98.70</td>
        <td>99.55</td>
        <td>98.30</td>
        <td>99.11</td>
    </tr>
    <tr>
        <td><b>Sugar Box</b></td>
        <td>99.20</td>
        <td>99.14</td>
        <td>-</td>
        <td>99.09</td>
        <td>99.37</td>
        <td>98.89</td>
        <td>99.75</td>
        <td>99.32</td>
        <td>99.54</td>
        <td>99.20</td>
        <td>99.28</td>
    </tr>
    <tr>
        <td><b>Tomato Soup Can</b></td>
        <td>98.40</td>
        <td>99.65</td>
        <td>99.26</td>
        <td>-</td>
        <td>99.40</td>
        <td>98.87</td>
        <td>98.86</td>
        <td>99.60</td>
        <td>99.00</td>
        <td>99.15</td>
        <td>99.13</td>
    </tr>
    <tr>
        <td><b>Mustard Bottle</b></td>
        <td>99.30</td>
        <td>98.90</td>
        <td>99.26</td>
        <td>99.90</td>
        <td>-</td>
        <td>98.87</td>
        <td>99.68</td>
        <td>98.95</td>
        <td>98.55</td>
        <td>98.95</td>
        <td>99.15</td>
    </tr>
    <tr>
        <td><b>Tuna Fish Can</b></td>
        <td>98.98</td>
        <td>99.28</td>
        <td>99.41</td>
        <td>98.98</td>
        <td>97.95</td>
        <td>-</td>
        <td>99.11</td>
        <td>99.13</td>
        <td>98.98</td>
        <td>99.28</td>
        <td>99.01</td>
    </tr>
    <tr>
        <td><b>Gelatin Box</b></td>
        <td>99.19</td>
        <td>99.40</td>
        <td>99.88</td>
        <td>99.51</td>
        <td>99.89</td>
        <td>99.33</td>
        <td>-</td>
        <td>98.81</td>
        <td>99.78</td>
        <td>99.03</td>
        <td>99.43</td>
    </tr>
    <tr>
        <td><b>Potted Meat Can</b></td>
        <td>99.20</td>
        <td>98.70</td>
        <td>99.03</td>
        <td>99.75</td>
        <td>98.30</td>
        <td>99.38</td>
        <td>98.81</td>
        <td>-</td>
        <td>98.90</td>
        <td>98.20</td>
        <td>98.92</td>
    </tr>
    <tr>
        <td><b>Mug</b></td>
        <td>98.80</td>
        <td>99.45</td>
        <td>99.49</td>
        <td>98.80</td>
        <td>98.70</td>
        <td>98.92</td>
        <td>99.51</td>
        <td>99.65</td>
        <td>-</td>
        <td>99.45</td>
        <td>99.20</td>
    </tr>
    <tr>
        <td><b>Large Marker</b></td>
        <td>98.30</td>
        <td>98.10</td>
        <td>99.43</td>
        <td>99.20</td>
        <td>98.95</td>
        <td>99.23</td>
        <td>99.24</td>
        <td>99.20</td>
        <td>99.55</td>
        <td>-</td>
        <td>99.03</td>
    </tr>
    <tr>
        <td><b>Average</b></td>
        <td>98.94</td>
        <td>99.10</td>
        <td>99.43</td>
        <td>99.31</td>
        <td>98.96</td>
        <td>99.08</td>
        <td>99.13</td>
        <td>99.17</td>
        <td>99.22</td>
        <td>98.93</td>
        <td>99.13</td>
    </tr>
    <tr>
      <td colspan="12"></td>
    </tr>
    <tr>
        <td><b>Complete Average</b></td>
        <td>98.99</td>
        <td>99.10</td>
        <td>99.36</td>
        <td>99.22</td>
        <td>99.06</td>
        <td>99.04</td>
        <td>99.28</td>
        <td>99.05</td>
        <td>99.21</td>
        <td>98.98</td>
        <td>&nbsp;</td>
    </tr>
</table>

### Training Performance
With respect to the training process, the PROPS datset had an initial period of little improvent much longer than CLEVR relative to total training time - the figure below shows only the first 9th of CLEVR training and improves much faster relative to its convergence. We theorize that real world data has more noise, leading to increased time to learn proper object embeddings.

<div class="center-image">
<table>
<tr>
  <td><img alt="PropsPlot" src="{{ site.baseurl }}/assets/projects/reports/props-relation/props_plot_cropped.webp" /></td>
  <td><img alt="CLEVRPlot" src="{{ site.baseurl }}/assets/projects/reports/props-relation/clevr_plot_cropped.webp" /></td>
</tr>
<tr>
  <td><div>CLEVR Dataset Results</div></td>
  <td><div>PROPS Dataset Results</div></td>
</tr>
</table>
</div>

## Other Dataset Use
We highly encourage you to checkout our code and train sornet on your own datasets! Checkout our example usage in our SORNET fork and our example implementaion for the PROPS dataset

<div class="project-links" markdown="1">
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Dataset Code](https://github.com/Jaldrich2426/PROPS-Relation-Dataset){: .btn .btn-grey .mr-6 target="_blank" rel="noopener noreferrer" }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Model Code](https://github.com/Jaldrich2426/sornet){: .btn .btn-grey target="_blank" rel="noopener noreferrer" }
</div>


To use this framework with another dataset, simply create a new file and overload the BaseRelationDataset class, following the exmaple in PropsRelationDataset. You need to overload each method that raises a "NotImplemented" error in the same manner as which PROPS does. If there is an existing dataset manager class, initialize it in the `_init_parent_dataset()` method of your derived class to make the implementation easier. Otherwise, load the appropriate file information in each class method and the base class should handle the relation information automatically, provided that the camera frame uses the standard notation.

If you would like to add further relations, simply overload the `get_spatial_relations()` method, and watch for any locations a "4" was hardcoded for the number of relations.

## Citation

If you found our work helpful, consider citing us with the following BibTeX reference:

```
@article{aldrich2024propsrelation,
  title = {Automatic Data Generation for SORNet: PROPS Relation Dataset},
  author = {Jace Aldrich, Ariana Verges Alicea, Hannah Ho},
  year = {2024}
}
```


## Contact

If you have any questions, feel free to contact [Jace Aldrich, Ariana Verges and Hannah Ho](mailto:jacealdr@umich.edu?cc=alarian@umich.edu,hdho@umich.edu).
