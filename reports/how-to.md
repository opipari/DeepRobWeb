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

---


#### Table of Contents

- [Abstract](#abstract)
- [Prerequisites](#prerequisites)
- [Building a Local Clone](#building-a-local-clone)
- [Inspecting an Example Project Page](#inspecting-an-example-project-page)
    - [Page Formatting](#page-formatting)
    - [Page Title](#page-title)
    - [Page Authors](#page-authors)
    - [Project Images](#project-images)
    - [Project Links](#project-links)
    - [Project Videos](#project-videos)
    - [Embedded Code](#embedded-code)
- [Adding a New Project Page](#adding-a-new-project-page)
- [Submitting a Pull Request to Publish your Page](#submitting-a-pull-request-to-publish-your-page)
- [Contact for Questions](#contact-for-questions)


{: .note-title }
> tl;dr
>
> You will describe the content on your page as a [markdown](https://en.wikipedia.org/wiki/Markdown){: target="_blank" rel="noopener noreferrer"} file (e.g. [this page is itself a markdown file](https://raw.githubusercontent.com/opipari/DeepRobWeb/w24/reports/how-to.md){: target="_blank" rel="noopener noreferrer"}). The markdown file gets converted by an application, called [Jekyll](https://en.wikipedia.org/wiki/Jekyll_(software){: target="_blank" rel="noopener noreferrer"}), into a static [HTML](https://en.wikipedia.org/wiki/HTML){: target="_blank" rel="noopener noreferrer"} file and is served on the internet at a specific domain (e.g. 'deeprob.com') and subdirectory (e.g. '/w24/reports/how-to/').





---



## Abstract

This tutorial is written to give a step-by-step tutorial on how your group can develop and design a final project webpage in the DeepRob 'style'. This tutorial involves concepts and tools used in web-development but we will assume no previous web-development experience.


---


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


---

## Building a Local Clone

Now that we have installed our software requirements and cloned the website source code, let's convert that source code into a working static site that we can add onto. 

Our goal here is to end up with an exact replica of [deeprob.org/w24/](https://deeprob.org/w24/){: target="_blank" rel="noopener noreferrer"} but which is entirely contained and served by your local development machine. Once this is working we can add a new page and modify it locally before pushing those changes into the official [DeepRob repository](https://github.com/opipari/DeepRobWeb){: target="_blank" rel="noopener noreferrer"} as a pull request. 

**Here are the steps to build our local site:**

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
Configuration file: /path.../DeepRobWeb/_config.yml
            Source: /path.../DeepRobWeb
       Destination: _site/w24/
 Incremental build: disabled. Enable with --incremental
      Generating... 
      Remote Theme: Using theme just-the-docs/just-the-docs
                    done in 15.273 seconds.
 Auto-regeneration: enabled for '/path.../DeepRobWeb'
    Server address: http://127.0.0.1:4000/w24/
  Server running... press ctrl-c to stop.
```
This message indicates a few noteworthy things:
1. The build worked without any errors and stored the resulting static site files in the `_site/w24/` directory
2. The build process took 15.273 seconds (it will be slightly faster on future builds)
3. The build is using `Auto-regeneration`, which just means that as long as this process keeps running, any changes to the source code in the `DeepRobWeb/` folder will automatically trigger the build process and update the served files
4. The server is running and hosting our static site at the location: [http://127.0.0.1:4000/w24/](http://127.0.0.1:4000/w24/){: target="_blank" rel="noopener noreferrer"}
5. We can stop the server by pressing `ctrl-c` or by closing the terminal window

{: .highlight }
**Note: This server is accessible only on your local development machine.** In other words, it is not publishing anything to the public internet. This is useful because it allows you to develop locally before publishing the final page to the public internet.

Now that the server is running, try navigating to the local site by going to the address: [http://127.0.0.1:4000/w24/](http://127.0.0.1:4000/w24/){: target="_blank" rel="noopener noreferrer"} in your browser. **If this doesn't work, or the website doesn't match the one published at [https://deeprob.org/w24/](https://deeprob.org/w24/){: target="_blank" rel="noopener noreferrer"}, please let [Anthony](mailto:topipari@umich.edu) know.**


---


## Inspecting an Example Project Page

Now that we have a local copy of the website, let's take a look at an example page for inspiration and direction on how we can design and structure our bew webpage. Specifically, looking into the [`reports/`](https://github.com/opipari/DeepRobWeb/tree/w24/reports){: target="_blank" rel="noopener noreferrer"} directory, we can see the source code used to generate this webpage as well as a simple example project page located at [`reports/example.md`](https://github.com/opipari/DeepRobWeb/blob/w24/reports/example.md){: target="_blank" rel="noopener noreferrer"}.


To get a better sense of how this example page works, let's open the local page side-by-side with its source code. The page can be opened at: [http://127.0.0.1:4000/w24/reports/example/](http://127.0.0.1:4000/w24/reports/example/){: target="_blank" rel="noopener noreferrer"}. The local page's source code, `reports/example.md`, can be opened with your favorite text editor. If all goes as planned, you should see a development environment similar to what's shown below:

![Development environment for example webpage]({{ site.baseurl }}/assets/projects/reports/how-to/development_environment.webp)

Next, let's step through the page elements one-by-one to understand how the markdown content is mapped onto HTML elements.


### Page Formatting

Taking a look at `reports/example.md`, the first thing we see is this header block:

```yaml
---
layout: project
parent: Reports
title: Example Project&#58; A final project template for DeepRob
description: This is a final project report for DeepRob at the University of Michigan.
authors:
  - name: Anthony Opipari
    social: "https://topipari.com"
    affiliation: University of Michigan
  - name: Xiaoxiao Du
    social: "https://xiaoxiaodu.net/"
    affiliation: University of Michigan
  - name: Edmond Tong
    affiliation: University of Michigan
  - name: Yifu Lu
    affiliation: University of Michigan
  - name: Dalton Richardson
    affiliation: University of Michigan
  - name: Odest Chadwicke Jenkins
    social: "https://ocj.name/"
    affiliation: University of Michigan
---
```

What's going on here? Well, this block of code is called ['front matter'](https://jekyllrb.com/docs/front-matter/){: target="_blank" rel="noopener noreferrer"} and is used by Jekyll to format the markdown content into a webpage. Front matter is essentially just a block of YAML code, storing key-value pairs of variables. Under the hood, while Jekyll is converting our markdown into an HTML page, it will use these variables for deciding how to organize the page's eventual HTML file.

**For formatting your project webpage, there are two required components you must include in your page's front matter:**

```yaml
layout: project
parent: Reports
```


<details markdown="block">
<summary>Click here for more details, if you're curious!</summary>>

The `layout` key is a generic front matter key specifying which HTML *scaffold* (or *layout*) to use when converting the markdown content *into* HTML. I've predefined an HTML structure for these project pages, which is defined by the `project` name. For those extra curious, you can inspect the `project` HTML layout definition in [`_layouts/project.html`](https://github.com/opipari/DeepRobWeb/blob/w24/_layouts/project.html){: target="_blank" rel="noopener noreferrer"}.

The `parent` key is used by our DeepRob theme, which is based on the [Just the Docs](https://just-the-docs.com/){: target="_blank" rel="noopener noreferrer"} theme, as a bookkeeping flag to ensure Jekyll doesn't clutter the navigation bar on the left of every page. Specifically, by using this key and assigning it a value of `Reports` we are telling Jekyll that the example project page shouldn't be shown on the navigation bar and that it belongs as a child page of the reports index at [`/w24/reports/`](https://github.com/opipari/DeepRobWeb/blob/w24/reports/index.md){: target="_blank" rel="noopener noreferrer"}.


</details>

### Page Title

Within the page front matter, we specify the title of the page. In the case of the example page:

```yaml
title: Example Project&#58; A final project template for DeepRob
```

Setting this value for `title` results in the title, `Example Project: A final project template for DeepRob`. The provided layout format will automatically position and format the title for you at the top of your project page in HTML. You'll notice we use `&#58;` where a colon is expected. This is because the colon, `:`, is a reserved character in YAML front matter but the character can be inserted with the proper escape (`&#58;`).


### Page Authors

The final key-value pair in our example front matter defines the page's authors. Specifically, this block:

```yaml
authors:
  - name: Anthony Opipari
    social: "https://topipari.com"
    affiliation: University of Michigan
  - name: Xiaoxiao Du
    social: "https://xiaoxiaodu.net/"
    affiliation: University of Michigan
  - name: Edmond Tong
    affiliation: University of Michigan
  - name: Yifu Lu
    affiliation: University of Michigan
  - name: Dalton Richardson
    affiliation: University of Michigan
  - name: Odest Chadwicke Jenkins
    social: "https://ocj.name/"
    affiliation: University of Michigan
```

Our provided project layout will format this list of authors into an equally-spaced row. Notice that the `social` attributes for each author are parsed into a proper weblink and that these attributes are optional: any authors that don't have an associated `social` attribute defined do not link to any external page.

### Project Images

Including a captivating image after the author list is a good strategy to summarize your project with a captivating visual element. The following code is used for placing the `deeprob.gif` file located in the `/w24/assets/projects/reports/example/` subdirectory within the example project page:

```html
<!-- This shows how to add an image (or gif) in markdown -->
<div class="center-image">
<img alt="Teaser Figure" src="{{ site.baseurl }}/assets/projects/reports/example/deeprob.gif" />
</div>
```

Notice that a css-class named `center-image` is applied as a parent element of our `img` element. The details can be ignored, but we provide this class to help you with centering images.

If we don't care about cenetering, we can more easily include images using the following command:

```markdown
![Teaser Figure]({{ site.baseurl }}/assets/projects/reports/example/deeprob.gif)
```


### Project Links

We provide default styling for any project-specific links you would like to include. For example, to include links to your report or your codebase, you can include the following code block below your front matter block:

```html
<div class="project-links" markdown="1">
[![]({{ site.baseurl }}/assets/logos/acrobat.svg){: .text-logo } Report](<PATH_TO_PDF>){: .btn .btn-grey .mr-6 target="_blank" rel="noopener noreferrer" }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Code](<PATH_TO_CODE>){: .btn .btn-grey target="_blank" rel="noopener noreferrer" }
</div>
```

where `<PATH_TO_PDF>` and `<PATH_TO_CODE>` are replaced with actual web links. This block of code results in the following buttons:

<div inert>
<div class="project-links" markdown="1">
[![]({{ site.baseurl }}/assets/logos/acrobat.svg){: .text-logo } Report](#){: .btn .btn-grey .mr-6 }
[![]({{ site.baseurl }}/assets/logos/github-mark.svg){: .text-logo } Code](#){: .btn .btn-grey }
</div>
</div>


### Project Videos

If you have any video results, those can be displayed either by using HTML video tags and hosting the video file with the `assets/` directory or by hosting the video on a service like YouTube. YouTube provides iframe HTML code that can be directly embedded into webpages as follows:

```html
<div class="video-wrap">
  <div class="video-container">
  <iframe src="https://www.youtube.com/embed/dx1G7y6mhMQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
</div>
```

Placing the above code into your markdown file will result in the following embeded iframe:

<div class="video-wrap">
  <div class="video-container">
  <iframe src="https://www.youtube.com/embed/dx1G7y6mhMQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
</div>


### Embedded Code

If you'd like to embed code, markdown provides [syntax highlighting](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks){: target="_blank" rel="noopener noreferrer"}. Simply wrap your code in backticks (\`) for in-line code or for code blocks, wrap your code in backtick-triplets.

````
```
# code goes here 
```
````

### Other Features!

Feel free to experiment with embedding content into your markdown webpage. For example, [plotly figures](https://plotly.com/chart-studio-help/embed-graphs-in-websites/){: target="_blank" rel="noopener noreferrer"} can be embedded into HTML--even [3D figures](https://plotly.com/python/3d-charts/){: target="_blank" rel="noopener noreferrer"}!

---

## Adding a New Project Page

Now that we've [inspected an example project page](#inspecting-an-example-project-page), we're ready to design our own! 

**Here are the required steps:**

1. Create a new markdown file (`.md`) and place it within the `reports/` directory
2. Fill in the markdown file's front matter block as described [above](#page-formatting)
3. Create a new asset directory with the same name as your markdown file and place the directory within `assets/projects/reports/`
4. Place any image, video, PDF, or other file assets you would like to host into your new asset directory
5. Add content to your webpage

---

## Submitting a Pull Request to Publish your Page

Now that you've made a webpage, let's make a pull request to the DeepRobWeb repository to publish your webpage on the internet.

**Here are the required steps:**

1. Fork the [DeepRobWeb](https://github.com/opipari/DeepRobWeb){: target="_blank" rel="noopener noreferrer"} repository

    ![Image of fork button on github graphic user interface]({{ site.baseurl }}/assets/projects/reports/how-to/fork_button.webp)

2. Make sure to uncheck the box asking if you want to copy only the `main` branch

    ![Image of fork options on github graphic user interface]({{ site.baseurl }}/assets/projects/reports/how-to/fork_options.webp)

3. Add your fork as a remote

    ```sh
    git remote add projectfork git@github.com:<your_user_name>/DeepRobWeb.git
    ```

4. Now sync your project with `origin` (i.e. the remote [DeepRobWeb](https://github.com/opipari/DeepRobWeb){: target="_blank" rel="noopener noreferrer"} repository)

    ```sh
    git pull origin w24
    ```

5. Now add any asset files and commit your changes

    ```sh
    git add <files> && git commit -m "Adding my final project webpage" <files>
    ```

6. We're now ready to push your changes into your forked repository
  
    ```sh
    git push projectfork w24
    ```

7. Next, checkout a new branch 

   ```sh
    git checkout -b <your_user_name>/final_project && push -u projectfork <your_user_name>/final_project
   ```

---

## Contact for Questions

If you have any questions, feel free to contact [Anthony](mailto:topipari@umich.edu).

---


[Back to Top](#)