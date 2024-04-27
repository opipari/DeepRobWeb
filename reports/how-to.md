---
layout: project
parent: Reports
title: How-To&#58; Make a project website for DeepRob
description: This is a tutorial showing how you can develop a final project webpage for DeepRob at the University of Michigan.
authors:
  - name: Anthony Opipari
    social: "https://topipari.com"
    affiliation: University of Michigan
---


{: .note-title }
> tl;dr
>
> You will describe the contents on your page as a [markdown](https://en.wikipedia.org/wiki/Markdown){: target="_blank" rel="noopener noreferrer"} file (e.g. [this page itself is a markdown file](https://raw.githubusercontent.com/opipari/DeepRobWeb/w24/reports/how-to.md){: target="_blank" rel="noopener noreferrer"}). The markdown file gets converted by an application, called [Jekyll](https://en.wikipedia.org/wiki/Jekyll_(software){: target="_blank" rel="noopener noreferrer"}), into a static [HTML](https://en.wikipedia.org/wiki/HTML){: target="_blank" rel="noopener noreferrer"} file and is served on the internet at a specific domain (e.g. 'deeprob.com') and subdirectory (e.g. '/w24/reports/how-to/').



## Abstract

This tutorial is written to give a step-by-step tutorial on how your group can develop and design a final project webpage in the DeepRob "style". This tutorial involves concepts and tools used in web-development but we will assume no previous web-development experience.




## Prerequisites

Before we can develop a new webpage and style it with our final project content, we need to install a useful set of web-development tools. Specifically, we need the Ruby programming language and the Jekyll application. Jekyll will be used for creating a local copy of the DeepRob website that we can develop ontop of while designing our new webpage. Jekyll is an application built with Ruby, and so we need Ruby for running Jekyll.

**On your local development machine:**
1. Install [Ruby](https://www.ruby-lang.org/en/documentation/installation/){: target="_blank" rel="noopener noreferrer"}
2. Install [Jekyll](https://jekyllrb.com/docs/installation/){: target="_blank" rel="noopener noreferrer"}
3. Clone the DeepRob source code

    ```sh
    git clone -b w24 git@github.com:opipari/DeepRobWeb.git
    ```


{: .highlight }
As part of the Ruby installation, another tool called '[Bundler](https://bundler.io/){: target="_blank" rel="noopener noreferrer"}' should be installed automatically. We'll use Bundler to manage our Ruby dependencies for building the static site with Jekyll.







## Contact

If you have any questions, feel free to contact [Anthony Opipari](mailto:topipari@umich.edu).

