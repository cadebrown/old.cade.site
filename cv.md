---
layout: default
title: Cade Brown &mdash; CV page
permalink: /cv
tag: cv
---

Hi! I'm Cade Brown, a software developer interested in machine learning, High Performance Computing (HPC), and programming language design

This is my CV, which contains my polished and published work. Please also check out the following links:

  * [cade.site/resume](/resume): my 1-page PDF resume
  * [cade.site/about](/about): short bio and information about me
  * [cade.site/timeline](/timeline): my complete timeline of work and projects

# Publications

**Design, Optimization, and Benchmarking of Dense Linear Algebra Algorithms on AMD GPUs**, Cade Brown, A. Abdelfattah, S. Tomov, and J. Dongarra, *2020 IEEE High Performance Extreme Computing Conference*, September 2020.

: TL;DR: We port the MAGMA library to AMD GPUs, got **60x faster** for some BLAS, and **73%** faster for Eigenvalue problems

: [Online PDF](/paper0.pdf)


## Other Publications

**SLATE Port to AMD and Intel Platforms**, A. Abdelfattah, M. Farhan, **Cade Brown**, M. Gates, D. Sukkari, A. YarKhan, J. Dongarra, *Innovative Computing Laboratory*, April 2021.

: TL;DR: We implement routines for the SLATE library on new AMD and Intel platforms. This is just a tech report publication

: [Online PDF](https://www.icl.utk.edu/files/publications/2021/icl-utk-1479-2021.pdf)


# Experience

## Innovative Computing Laboratory {#icl}

_Research Assistant in HPC, ML (2019-Present in Knoxville, TN, US)_

I am currently working as a student researcher with [Stan Tomov](https://scholar.google.com/citations?user=HFzflUwAAAAJ&hl=en), [Jack Dongarra](https://en.wikipedia.org/wiki/Jack_Dongarra), and [Piotr Luszczek](https://scholar.google.com/citations?user=a9df4xQAAAAJ&hl=en) in various areas, including High Performance Computing (HPC) and Machine Learning (ML/AI).

  * **Ported and performance-tuned** the MAGMA linear algebra library for new AMD GPU hardware
  * **Improved performance** 60x faster for certain BLAS, 73% faster for Eigenvalue problems
  * **Wrote and published a paper** analyzing the performance of MAGMA vs vendor implementations, published in IEEE HPEC: **[cade.site/paper0](https://cade.site/paper0)**
  * **Implemented GPU compute kernels** for the SLATE project: **[cade.site/slate](https://cade.site/slate)**

## PAIRS Laboratory {#pairs}

_Research Assistant in HCI, PLT (2021-2022 in Knoxville, TN, US)_

I worked as a research assistant to [Austin Henley](http://austinhenley.com/) for a period of time at the PAIRS lab, which was a short-lived Human-Computer Interaction (HCI) lab that focused on developer efficiency and program analysis.

 * **Implemented a research prototype** of Avocat, an automated error solver for the terminal
 * **Evaluated and improved** performance of database queries for WorldSyntaxTree, a terabyte-scale graph database of source code

## Oak Ridge National Laboratory {#ornl}

_Research Assistant in HPC, distributed computing (2017-2018 in Oak Ridge, TN, US)_

I worked as an intern as a part of the [SimpleSummit](https://simplesummit.github.io) project. I wrote the interactive simulation software, and assisted with the physical fabrication of the prototype.

 * **Used CUDA, MPI, and SDL** to build a realtime distributed fractal rendering application/simulation
 * **Programmed the NVIDIA Jetson platform** to divide and distribute the workload between 8 nodes (CPU & GPU) over a local network
 * **Coordinated with ORNL's MDF** for physical fabrication of the cluster computer's case
 * **Used Jekyll, HTML, and GitHub** to build a public website: **[simplesummit.github.io](https://simplesummit.github.io)**

# Projects

__NOTE__: These are just my polished, released projects. For all my personal projects, check out my timeline: [cade.site/timeline](https://cade.site/timeline)


## kscript {#kscript}

I wrote kscript ([kscript.org](https://kscript.org)), which is a dynamic programming language with support for tensors, math routines, graphics and more. It has an online repl: [term.kscript.org](https://term.kscript.org) and documentation: [docs.kscript.org](https://docs.kscript.org)

## Cade Andgreg's RISC-V Emulator {#kscript}

I worked on a team to design and implement a web-based IDE for RISC-V programming and debugging: [carve.chemicaldevelopment.us](https://carve.chemicaldevelopment.us)


## Online Encyclopedia of Integer Sequences {#oeis}

I made various contributions to sequences and discussions, as a hobby interest of mine

  * **Authored sequence A267263**, the number of nonzero digits in representation of n in primorial base: **[oeis.org/A267263](https://oeis.org/A267263)**
  * **Assissted sequence A277313**, gave hueristics and example program: **[oeis.org/A277313](https://oeis.org/A277313)**
