---
layout: default
title: About
permalink: /about
---

## About

Hello there! My name is Cade Brown, and this is my [personal blog](https://cade.site). I'm a programmer, mathematician and musician, and i like writing about it!

Important links:

  * [me@cade.site](mailto:me@cade.site), my personal email (my preferred contact method)
  * [github.com/cadebrown](https://github.com/cadebrown), my GitHub (this is where most of my code happens)
  * [/timeline](/timeline), timeline of my major projects and important dates
  * [/files/resume-CadeBrown-2021-10-01.pdf](/files/resume-CadeBrown-2021-10-01.pdf), my resume

My main areas of interest are:

  * Programming Language Theory (PLT), including esoteric languages and language design
  * Mathematical programming/algorithms (like bignum arithmetic, root finding, symbolic algebra)
  * GPU/heterogeneous computing (like CUDA, HIP, OpenCL, ...)

Currently, i'm working on:

  * [kata.tools](https://kata.tools): a WIP software framework, runtime, and set of languages to rule them all!


## Projects


### MAGMA (Matrix Algebra on GPU and Many-core Architectures)

At ICL, i have been working on the [MAGMA](https://icl.utk.edu/magma/) project, specifically adding the abilitity to run on AMD GPUs via the HIP platform (previously, it was primarily CUDA-focused). i also worked on tuning our algorithms for better performance on the new hardware.

[check out my paper!](https://www.icl.utk.edu/files/publications/2020/icl-utk-1415-2020.pdf)

### "Know It All", an A.i. writer

I (along with Jakob Liggett) worked on ["Know It All"](https://www.youtube.com/watch?v=PwGsRskWN-i) as part of the UTK VolHacks hackathon. It is a machine-learning based program which listens for audio input, transcribes it, and then completes the quote, using the GPT-2 algorithm

It turned out quite well, and the video above has some amusing, meta-textual responses


### SimpleSummit, a distributed computing project 

[SimpleSummit](https://simplesummit.github.io/) was my project during 2 successive summer internships at ORNL at the OLCF. It is a small cluster computer made of [NVIDIA Jetsons](https://developer.nvidia.com/buy-jetson), and can, in real time, use multiprocessing to allow a user to view a fractal in real time.

I did all of the software for the project, which included `fractalexplorer`. It ran over 8 different machines at once, which communicated in real time (via MPI) over a network to produce ~30fps fractal rendering.

Check out our ORNL article here: [SimpleSummit](https://www.olcf.ornl.gov/2018/10/09/simple-summit/)

