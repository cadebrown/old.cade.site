---
layout: post
title: "Dense Linear Algebra Algorithms on AMD GPUs"
tags: [math, work]
thumb: /files/magma-figure2.webp
---

I'm excited to have recently published my first journal paper with ICL! You can check it out on [HGPU](https://hgpu.org/?p=22887). TL;DR: we port a math library to AMD GPUs and get much better performance than AMD's existing vendor libraries

<!--more-->

You can check out the paper at the bottom of this page, or at [this URL](https://www.icl.utk.edu/files/publications/2020/icl-utk-1405-2020.pdf)

I wrote this paper with Ahmad Abdelfattah, Stan Tomov, and Jack Dongarra at the Innovative Computing Laboratory, while a research assistant. We used auto-translation tools to convert the source code (in addition to some manual changes) to port from the existing CUDA platform to the new HIP/ROCm platform.

While doing this, we also did performance tuning on algorithms, specifically aimed at improving performance on the new AMD hardware. There are a number of differences (such as warp size, memory hierarchy, and compiler optimizations) that allowed us to improve performance, bringing it a lot closer to the peak performance on these GPUs.


## References

My paper was added to the [OS hackathon resources page](https://www.oshackathon.org/resources#h.2swl4wedmt8y)

<iframe src="https://www.icl.utk.edu/files/publications/2020/icl-utk-1405-2020.pdf" style="width:100%; height:900px;" frameborder="0"></iframe>
