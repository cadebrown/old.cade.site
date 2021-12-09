---
layout: default
title: About
permalink: /about
---

## About

Hello there! My name is Cade Brown, and this is my [personal blog](https://cade.site). I'm a software developer and a musician.




Useful Links:

  * [me@cade.site](mailto:me@cade.site), my personal email (my preferred contact method)
  * [github.com/cadebrown](https://github.com/cadebrown), my GitHub (this is where most of my code happens)
  * [/timeline](/timeline), timeline of my major projects and important dates
  * [/files/resume-CadeBrown-2021-12-08.pdf](/files/resume-CadeBrown-2021-12-08.pdf), my resume

My main areas of interest are:

  * Programming Language Theory (PLT), including esoteric languages and language design
  * Numerical/math programming (like bignum arithmetic, root finding, symbolic algebra)
  * GPU/heterogeneous computing (like CUDA, HIP, OpenCL, ...)

Currently, I'm working on:

  * [kata.tools](https://kata.tools): a WIP software framework, runtime, and set of languages to rule them all!
  * [Avocat](https://github.com/utk-pairs/avocat): Avocat is an automated error-solver for your terminal!


## Projects


### MAGMA and SLATE, HPC Libraries

At ICL, I worked on the [MAGMA](https://icl.utk.edu/magma/) project, specifically, the abilitity to run on AMD GPUs via the ROCm/HIP platform (previously, it was primarily CUDA-focused). I also worked on tuning DLA algorithms for better performance on existing NVIDIA hardware.

I also worked part-time on the [SLATE](https://icl.utk.edu/slate/) project, porting backends to use rocBLAS and OpenMP (for AMD and Intel platforms, respectively).

[Design, Optimization, and Benchmarking of Dense
Linear Algebra Algorithms on AMD GPUs](https://www.icl.utk.edu/files/publications/2020/icl-utk-1415-2020.pdf)


### "Know It All", an A.I. writer

I (along with Jakob Liggett) worked on ["Know It All"](https://www.youtube.com/watch?v=PwGsRskWN-i) as part of the UTK VolHacks hackathon. It is a machine-learning based program which listens for audio input, transcribes it, and then continues the quote, using the GPT-2 algorithm

It turned out quite well, and the video above has some amusing, meta-textual responses. Since then, GPT-3 has come out (along with free variants), which would undoubtedly increase the quality of the continuations.


### SimpleSummit, a distributed computing project 

[SimpleSummit](https://simplesummit.github.io/) was my project during 2 successive highschool internships at ORNL at the OLCF. It is a small cluster computer made of a few [NVIDIA Jetsons](https://developer.nvidia.com/buy-jetson), hooked up over a network. The network adapts in real time to distribute the workload evenly, taking into account the real-time metrics of the cluster.

I did all of the software for the project, which included `fractalexplorer`. It ran over 8 different machines at once, which communicated in real time (via MPI) over a network to produce ~30fps fractal rendering.

Check out our ORNL article here: [SimpleSummit](https://www.olcf.ornl.gov/2018/10/09/simple-summit/)

