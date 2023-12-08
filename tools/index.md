---
layout: page
title: Tools
description: Collection of deep learning tools and frameworks.
nav_order: 5
has_children: false
has_toc: true
---

# Deep Learning Tools and Frameworks
{:.no_toc}

A collection of tools and projects that support deep learning applications to robotic tasks. Within each category below, the course staff provides a sample of tools that may be helpful for implementing course and research projects with deep learning.

---

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---




## Learning Frameworks

Deep Learning frameworks speed-up model development and testing by providing users with optimized implementations of low-level functions (automatic differentiation, gradient descent, matrix operations, etc.) that can be used as building-blocks for robot applications.


<hr class="hr-text" content="Python">
Open-source python-based deep learning frameworks have fostered a community and set of tools responsible for many of the core research and engineering developments powering deep learning. Here are some of the most popular python-based frameworks:

<div style="text-align: center;">

	<div style="display:flex; verticle-align: middle; justify-content: space-evenly;">

		<div class="logo-container">
			<a href="https://pytorch.org" target="_blank" rel="noopener noreferrer" class="logo-link">
				<img src="{{ site.baseurl }}/assets/logos/external/pytorch.svg" alt="Link to PyTorch software website" class="footer-img" >
			</a>
		</div>

		<div class="logo-container">
			<a href="https://jax.readthedocs.io/" target="_blank" rel="noopener noreferrer" class="logo-link">
				<img src="{{ site.baseurl }}/assets/logos/external/JAX.svg" alt="Link to JAX software website" class="footer-img" >
			</a>
		</div>

		<div class="logo-container">
			<a href="https://www.tensorflow.org" target="_blank" rel="noopener noreferrer" class="logo-link">
				<img src="{{ site.baseurl }}/assets/logos/external/TF.svg" alt="Link to TensorFlow software website" class="footer-img" >
			</a>
		</div>

		<div class="logo-container">
			<a href="https://www.paddlepaddle.org.cn/" target="_blank" rel="noopener noreferrer" class="logo-link">
				<img src="{{ site.baseurl }}/assets/logos/external/paddle.png" alt="Link to PaddlePaddle software website" class="footer-img" >
			</a>
		</div>
	</div>
</div>

<br>

<hr class="hr-text" content="C and C++">

While Python-based learning frameworks typically offer C-APIs, they have been built-on and inspired-by additional open-source projects, including:

<div style="text-align: center;">

	<div style="display:flex; verticle-align: middle; justify-content: space-evenly;">

		<div class="logo-container">
			<a href="https://pjreddie.com/darknet/" target="_blank" rel="noopener noreferrer" class="logo-link">
				<img src="{{ site.baseurl }}/assets/logos/external/darknet.png" alt="Link to Darknet software website" class="footer-img" >
			</a>
		</div>

		<!-- <div class="logo-container">
			<a href="https://pjreddie.com/darknet/nightmare/" target="_blank" rel="noopener noreferrer" class="logo-link">
				<img src="{{ site.baseurl }}/assets/logos/external/nightmare.png" alt="Link to Nightmare software website" class="footer-img" >
			</a>
		</div> -->

		<div class="logo-container">
			<a href="https://caffe.berkeleyvision.org" target="_blank" rel="noopener noreferrer" class="logo-link">
				<img src="{{ site.baseurl }}/assets/logos/external/caffe.png" alt="Link to Caffe software website" class="footer-img" >
			</a>
		</div>

		<div class="logo-container">
			<a href="https://caffe2.ai" target="_blank" rel="noopener noreferrer" class="logo-link">
				<img src="{{ site.baseurl }}/assets/logos/external/caffe2.png" alt="Link to Caffe2 software website" class="footer-img" >
			</a>
		</div>
	</div>
</div>


<br>

<hr class="hr-text" content="Julia">

The more recent language, Julia, which you may be familiar with through the [ROB curriculum](https://robotics.umich.edu/academic-program/course-offerings/rob101/){: target="_blank" rel="noopener noreferrer"}, also offers deep learning support:

<div style="text-align: center;">

	<div style="display:flex; verticle-align: middle; justify-content: space-evenly;">

		<div class="logo-container">
			<a href="https://fluxml.ai/Flux.jl/stable/" target="_blank" rel="noopener noreferrer" class="logo-link">
				<img src="{{ site.baseurl }}/assets/logos/external/flux.png" alt="Link to Flux software website" class="footer-img" >
			</a>
		</div>

		<div class="logo-container">
			<a href="https://alan-turing-institute.github.io/MLJ.jl/" target="_blank" rel="noopener noreferrer" class="logo-link">
				<img src="{{ site.baseurl }}/assets/logos/external/mlj.svg" alt="Link to MLJ software website" class="footer-img" >
			</a>
		</div>

		
	</div>
</div>





## Library Ecosystem

A vast number of specialized software libraries have been built upon the popular open-source learning frameworks to provide data structures and algorithms that are customized to specific domains and use-cases. Often, these provide optimized implementations that are useful for a specific group of developers working within a specific sub-area of robot learning while also facilitating interactions and collaborations within the community. Contributing to these open-source projects is valuable and encouraged. Here are a sample that may be related to your interests:

 - [PyTorch3D](https://pytorch3d.org/){: target="_blank" rel="noopener noreferrer"}: a specialized library for integrating 3D data (points, geometries, renderers, etc.) with deep learning in PyTorch

 - [nerfstudio](https://docs.nerf.studio/){: target="_blank" rel="noopener noreferrer"}: for implementing, training, visualizing, and exporting your Neural Radiance Fields

 - [Ray](https://docs.ray.io/en/latest/){: target="_blank" rel="noopener noreferrer"}: a library for scalable reinforcement learning

 - [GPyTorch](https://gpytorch.ai/){: target="_blank" rel="noopener noreferrer"}: for implementing Gaussian Processes in with GPU-acceleration in PyTorch



## Data Annotation

Much of deep learning ([but not all]({{ site.baseurl }}/papers/#self-supervised-learning)) relies on human-annotated data for training or evaluation. The data and annotations are typically expensive to obtain, which motivates the development and use of tools to make data annotation more efficient and cheaper. Here are a small sample of tools that exist to support your labeling efforts:

 - [Voxel51](https://voxel51.com/fiftyone/){: target="_blank" rel="noopener noreferrer"}

 - [LabelStudio](https://labelstud.io/){: target="_blank" rel="noopener noreferrer"}

 - [CVAT: Computer Vision Annotation Tool](https://www.cvat.ai/){: target="_blank" rel="noopener noreferrer"}

 - [3D BAT: Bounding Box Annotation Tool](https://github.com/walzimmer/3d-bat){: target="_blank" rel="noopener noreferrer"}

 - [ProgressLabeller](https://progress.eecs.umich.edu/projects/progress-labeller/){: target="_blank" rel="noopener noreferrer"}

 - [6D-PAT: Pose Annotation Tool](https://github.com/florianblume/6d-pat){: target="_blank" rel="noopener noreferrer"}



## Simulation Environments

Robots and sensors can be prohibitively expensive, so simulation environments have been created to enable large-scale training (i.e. [reinforcement learning]({{ site.baseurl }}/papers/#reinforcement-learning)) and data collection within robotics. Here are a few to get you started:

 - [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim){: target="_blank" rel="noopener noreferrer"}

 - [AI2THOR](https://ai2thor.allenai.org/){: target="_blank" rel="noopener noreferrer"}

 - [PyBullet](https://pybullet.org/){: target="_blank" rel="noopener noreferrer"}

 - [Gymnasium](https://gymnasium.farama.org/){: target="_blank" rel="noopener noreferrer"}



## Visualization

Understanding model architectures and outputs is crucial to validate and develop useful deep learning-based systems. Visualization tools can help support our understanding, especially for perception tasks, by depicting model predictions. Knowing which tools are useful for a given modality and how to use those tools is valuable skill for deep learning practicioners. Here are some visualization tools that are broadly useful:


 - [TensorBoard](https://www.tensorflow.org/tensorboard){: target="_blank" rel="noopener noreferrer"}: to understand model architectures and summary statistics measured during training

 - [Open3D](http://www.open3d.org/){: target="_blank" rel="noopener noreferrer"}: for visualizing 3D data modalities

 - [Plotly](https://plotly.com/python/){: target="_blank" rel="noopener noreferrer"}: for general purpose analysis and plotting

 - [RViz](http://wiki.ros.org/rviz){: target="_blank" rel="noopener noreferrer"}: for integrating visualization with ROS topics




## Model Formats

Open-source model formats describe learning-based architectures and models in order to enable sharing and deploying the models independent of the software-hardware used during model training and development. These are especially useful for deploying the models, where minimizing latencies caused by the general-purpose learning frameworks can be crucial.

 - [ONNX: Open Neural Network Exchange](https://onnx.ai/){: target="_blank" rel="noopener noreferrer"}

 - [NNEF: Neural Network Exchange Format](https://www.khronos.org/nnef/){: target="_blank" rel="noopener noreferrer"}


## Misc

 - [distill.pub](https://distill.pub/guide/){: target="_blank" rel="noopener noreferrer"}: for organizing your publications in an elegant and shareable format

 - [ConvNetJS](https://cs.stanford.edu/people/karpathy/convnetjs/): A minimal Javascript library for neural network training and inference within web-browsers

