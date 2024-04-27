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

This tutorial is written to give a step-by-step tutorial on how your group can develop and design a final project webpage in the DeepRob 'style'. This tutorial involves concepts and tools used in web-development but we will assume no previous web-development experience.




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



## Building a Local Clone

Now that we have installed our software requirements and cloned the website source code, let's convert that source code into a working static site that we can add onto. 

Our goal here is to end up with an exact replica of [deeprob.org/w24/](https://deeprob.org/w24/) but which is entirely contained and served by your local development machine. Once this is working we can add a new page and modify it locally before pushing those changes into the official DeepRob website. Here are the steps to build our local site:

1. Open a terminal window
2. Navigate to the root directory of the cloned w24 repository

    ```sh
    cd DeepRobWeb
    ```
3. Install the Ruby gem dependencies needed to build the static

    ```sh
    bundle install 
    ```
4. Build and serve the static site locally

    ```sh
    bundle exec jekyll serve
    ```

After running the above commands, you should see terminal output similar to what's shown below:

```sh
Configuration file: /path.../DeepRob/_config.yml
            Source: /path.../DeepRob
       Destination: _site/w24/
 Incremental build: disabled. Enable with --incremental
      Generating... 
      Remote Theme: Using theme just-the-docs/just-the-docs
                    done in 15.273 seconds.
 Auto-regeneration: enabled for '/path.../DeepRob'
    Server address: http://127.0.0.1:4000/w24/
  Server running... press ctrl-c to stop.
```
This message indicates a few noteworthy things:
1. The build worked without any errors and stored the resulting static site files in the ` _site/w24/` directory
2. The build process took 15.273 seconds (it will be slightly faster on future builds)
3. The server is running and hosting our static site at the location: [http://127.0.0.1:4000/w24/](http://127.0.0.1:4000/w24/){: target="_blank" rel="noopener noreferrer"}
4. We can stop the server by pressing `ctrl-c` or by closing the terminal window

Now that the server is running, try navigating to the local site by going to the address: [http://127.0.0.1:4000/w24/](http://127.0.0.1:4000/w24/){: target="_blank" rel="noopener noreferrer"} in your browser. **If this doesn't work, or the website doesn't match the one published at [https://deeprob.org/w24/](https://deeprob.org/w24/){: target="_blank" rel="noopener noreferrer"}, please let [Anthony](mailto:topipari@umich.edu) know.**




## Contact

If you have any questions, feel free to contact [Anthony](mailto:topipari@umich.edu).

