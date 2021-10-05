---
layout: default
title: About
permalink: /about
---

## About

Hey there! My name is Cade Brown, and this is my personal blog ([https://cade.site](https://cade.site)). I'm currently working as a Research Assistant to [AZH](http://web.eecs.utk.edu/~azh/). You can check out my resume here: [resume-CadeBrown.pdf](/files/resume-CadeBrown.pdf), or read my full history on this page

This site covers many of my own personal programming, math, and life adventures. You should also check out my [kata.tools](https://kata.tools) site, which has a dev blog for that project.


## Biography

This is a high-level biography of my life/career/interests:

  * 2001-02-13: My birthday! during [the Timequake](https://en.wikipedia.org/wiki/Timequake), and [the Earthquake](https://en.wikipedia.org/wiki/Portal:Current_events/February_2001), in Knoxville, TN
  * Started playing piano, taking classical piano lessons in ~2006
  * Started programming in ~2007 in C#, Scratch, Alice3D
  * Started programming in ~2011 in Java, Python
  * Started programming in ~2014 in C, JavaScript
  * Contributed to [OEIS](https://oeis.org/A277313), including [my own integer sequence](https://oeis.org/A267263)
  * Contributed bug fixes, and corresponding test cases for special functions in [GNU MPFR](https://www.mpfr.org/)
    * If your computer has a modern version of GCC, my code is probably on your computer
  * Developed plugins for bukkit: [gamble](https://dev.bukkit.org/projects/cade-gamble), [my account](https://dev.bukkit.org/members/_ForgeUser14038486/projects)
  * Went to L&N STEM Academy, graduating high school in 2019
  * Programmed robots as part of the [L&N STEMpunks FRC #3966 team](https://www.youtube.com/c/LNSTEMpunksorg/videos), and was Programming Leader for that time as well (a total of 3 years on the team, during highschool)
  * Deep-dove into fractals, rendering, and distributed computing in 2015-2016 (see [fractalrender](https://github.com/chemicaldevelopment/fractalrender), [my post for fractalexplorer/SimpleSummit](https://simplesummit.github.io/blog/fractalexplorer))
    * check out a video I made [here](https://www.youtube.com/watch?v=ynSdQAhDoWQ)
  * In 2015, I worked on a low-cost and small form factor data logger solution (pilog) for air-quality monitoring for [Agilaire](https://agilaire.com/)
  * Started programming in ~2016 in [ezc](https://github.com/ChemicalDevelopment/ezc)
  * From 2016-2017, I worked at ORNL on [SimpleSummit](https://simplesummit.github.io/) for 2 consecutive summer internships
  * Did a lot of research related to prime searching, including [PGS (Prime Generator Search)](https://github.com/ChemicalDevelopment/PGS)
    * `359 + 558*x + 36*x**2` is prime for x = 0, 1, ... 28, 29 (i.e. 30 consecutive values)
  * Started programming in ~2019 in [kscript](https://ksript.org)/katascript (my own programming language)
    * The documentation is available: [https://docs.kscript.org/](https://docs.kscript.org/)
    * Wanna try it? We have a [web demo](https://term.kscript.org/) available
  * Attended UTK, 2019-fall, B.S. in Computer Science expected 2023
  * Made "Know It All", an AI-writer [see how it works](https://www.youtube.com/watch?v=PwGsRskWN-I&t=3s)
  * Wrote some [gravity simulations](https://www.youtube.com/watch?v=rbCcHSDHe34)
    * [Here's](https://www.youtube.com/watch?v=m--zadaNnI0) one I did in Unity
  * Wrote my first paper, in 2020: ["Design, Optimization, and Benchmarking of Dense Linear Algebra Algorithms on AMD GPUs"](https://ieeexplore.ieee.org/document/9286214) (published in IEEE HPEC w/ Jack Dongarra, Stanimere Tomov, and Ahmad Abdelfattah as other authors)
  * I've been 1/3 of [Dysmorphic Demiurge](https://www.metal-archives.com/bands/Dysmorphic_Demiurge/3540466961), as a death metal vocalist and producer
  * I made a Minecraft-like game, [Blok](https://github.com/CadeBrown/Blok) from scratch
  * I've released a number of electronic music albums/songs:
    * [Cade Brown - "All Things Are Nothing To Me"](https://www.youtube.com/watch?v=5gu5sbaA1EE)
    * [ghoti - "ghoti[0]"](https://www.youtube.com/watch?v=FAfwOztmb28&list=OLAK5uy_n3wgIoUN7xbJpmPYvueyTewwP-eGxQzo0)
  * Worked at [ICL@UTK](https://www.icl.utk.edu/) from 2019-2021, working on [MAGMA](https://icl.cs.utk.edu/magma/) and [SLATE](http://icl.utk.edu/slate/)
  * Primary developer of the [kata.tools](https://kata.tools) project, starting in 2021


## Projects

### kscript (Programming Language)

On my own time, I have been working on [kscript](https://kscript.org), which is a dynamic programming language with a rich standard library. I am responsible for >95% of the code, and am the owner of the project. I have high hopes for reaching a large audience after an alpha release is done as a proof of concept, alongside tutorials showing how easy it is to use.


### MAGMA (Matrix Algebra on GPU and Many-core Architectures)

At ICL, I have been working on the [MAGMA](https://icl.utk.edu/magma/) project, specifically adding the abilitity to run on AMD GPUs via the HIP platform (right now it is NVIDIA/CUDA only).


### "Know It All", an A.I. writer

I (along with Jakob Liggett) worked on ["Know It All"](https://www.youtube.com/watch?v=PwGsRskWN-I) as part of the UTK VolHacks hackathon. It is a machine-learning based program which listens for audio input, transcribes it, and then completes the quote, using the GPT-2 algorithm

It turned out quite well, and the video above has some amusing, meta-textual responses


### SimpleSummit, a distributed computing project 

[SimpleSummit](https://simplesummit.github.io/) was my project during 2 successive summer internships at ORNL at the OLCF. It is a small cluster computer made of [NVIDIA Jetsons](https://developer.nvidia.com/buy-jetson), and can, in real time, use multiprocessing to allow a user to view a fractal in real time.

I did all of the software for the project, which included `fractalexplorer`. It ran over 8 different machines at once, which communicated in real time (via MPI) over a network to produce ~30fps fractal rendering.

Check out our ORNL article here: [SimpleSummit](https://www.olcf.ornl.gov/2018/10/09/simple-summit/)

