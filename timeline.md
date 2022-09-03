---
layout: default
title: Timeline
permalink: /timeline
use_jquery: true
use_katex: true
---

If you're looking for the TL;DR, check out [my resume (PDF)](/resume-CadeBrown.pdf).


# Timeline

2022-05 - [NVIDIA Internship](https://nvidia.com)

  : At my NVIDIA internship, I worked on the Machine Learning Compiler team’s internal projects that improve compute performance for popular AI workloads (matrix multiplication, convolution, tensor operations). We use polyhedral compilation techniques mapped directly to NVIDIA GPU hardware, which takes advantage of warp communication, shared memory, memory pipelining, and hardware tensor cores (MMA). I wrote performance tuning software to search and select optimizations to compete with cuBLAS on modern NVIDIA GPUs.

  : Using large performance datasets I generated, I trained a Machine Learning model to learn how to compile efficient GPU kernels, based on millions of performance data points. This work can be integrated into an ML runtime (such as PyTorch) to optimize computations in real time via a Just-In-Time (JIT) interface for GPU kernel compilation.

  : Most of this internship is under a NDA
  
<!--

2021-08 - [kata.tools](https://kata.tools), [*.ks](https://ks.kata.tools)

  : Kata is an open-source cross-platform ecosystem for developing software on desktop, mobile, web, and HPC platforms

  : I am the creator and primary developer of Kata

  : NOTE: project is currently in pre-alpha stages, not intended for public use
-->

2021-07 - [Avocat](https://github.com/utk-pairs/avocat)

  : Avocat is an assistant for the terminal, that attempts to automatically complete tasks and resolve errors
  
  : I wrote the core execution logic, and my colleague [Gregory Croisdale](https://gregory.croisdale.us/) also worked on the project

2021-06 - [ML/AI Art](https://github.com/cadebrown/cmlart)

  : Check out my blog post, [here: /2021/11/12/art-aigen](/2021/11/12/art-aigen)

  : I wrote some ML/AI utilities, as well as used some pre-existing models to generate pictures and videos

  : Check out this video I helped produce for my band: [Beneath The Catacombs of Celephaïs](https://www.youtube.com/watch?v=wWBboUDMPw4)

  : ![Album Art for "Societas de Machinarum XIII"](/files/album-societas-de-machinarum-xiii.webp)

2021-05 - [Dysmorphic Demiurge - DEREALIZATION](https://www.youtube.com/watch?v=ugiHrij0CfY)

  : My death metal band, [Dysmorphic Demiurge](https://www.facebook.com/DysmorphicDemiurge/) released an album, [DEREALIZATION](https://www.youtube.com/watch?v=ugiHrij0CfY). I'm the primary vocalist, and I do some of the production elements

  : Completely self-produced, this album is an hour of intense technical music with changing time signatures, tempo, and mood. I highly recommend you check it out, if you're interested in this kind of music!

  : Released on [Miasma Records](https://miasmarecords.com/collections/dysmorphic-demiurge)

  : ![Album Art for "DEREALIZATION"](/files/DDD.webp)

2021-02 - [CARVE (Cade Andgreg's Risc-V Emulator)](https://carve.chemicaldevelopment.us/)

  : CARVE is a RISC-V emulator for the web, written by me and Gregory Croisdale. Features a debugger

  : CARVE is written in C, compiled to WebAssembly and can be ran on any browser that supports WASM (most browsers, mobile and desktop)

2020-04 - [Dysmorphic Demiurge - As You Hunger For Pardon](https://www.metal-archives.com/bands/Dysmorphic_Demiurge/3540466961)

  : My death metal band, [Dysmorphic Demiurge](https://www.facebook.com/DysmorphicDemiurge/) released an album, [As You Hunger For Pardon](https://www.youtube.com/watch?v=R-aQyCgwTpk)

  : I'm the primary vocalist, and I do some of the production elements. This was our first album, released on Inherited Suffering Records

2020-06 - [HEARO (Qardian Labs)](https://www.qardianlabs.net/)

  : I designed and trained a machine learning model for 14-point evaluations of heart disease risk, scoring ~91% accuracy on the test set (with 80/20 validation and shuffling), as well as a web interface for the model

  : [Here's a working demo](https://radiant-mesa-06241.herokuapp.com/HEARO14/)

2020-05 - [SLATE (HIP port)](http://icl.utk.edu/slate/)

  : SLATE is a linear algebra library aimed at exascale computing. I worked on porting some parts to the HIP/ROCm stack

  : Here's the [published working notes](https://www.icl.utk.edu/files/publications/2021/icl-utk-1479-2021.pdf)

2020-03 - ["Design, Optimization, and Benchmarking of Dense Linear Algebra Algorithms on AMD GPUs"](https://ieeexplore.ieee.org/document/9286214)

  : TL;DR: successfully ported to HIP with automatic source transpilation, 2x-20x speedup on some BLAS routines, 58%-75% speedup on some LAPACK routines. Check out [my blog post](/2020/magma-paper)

  : Here's the [published paper](https://www.icl.utk.edu/files/publications/2020/icl-utk-1405-2020.pdf)

  : ![chart from paper](/files/paper-icl0-chart0.webp)

2019-09 - ["Know It All", an AI Writer](https://www.youtube.com/watch?v=PwGsRskWN-I)

  : A [VolHacks](https://volhacks.org/) project that listens to your voice and continues to write a story for you (outdated now, of course, due to new developments in GPT-3)

  : This was a joint effort between myself and Jakob Liggett

2019-08 - [MAGMA (HIP port, optimization)](https://icl.cs.utk.edu/magma/)

  : MAGMA is a linear algebra library aimed at GPU/many-core systems, largely as a modern replacement for [LAPACK](https://en.wikipedia.org/wiki/LAPACK)

  : I worked on porting the entire library to the HIP/ROCm stack, as well as optimization of the existing algorithms for better performance on both existing hardware (NVIDIA GPUs) and the new hardware just supported (AMD GPUs). 

  : Here's the [published paper](https://www.icl.utk.edu/files/publications/2020/icl-utk-1405-2020.pdf)

2019-01 - [kscript (programming language)](https://kscript.org)

  : Superseded by [kata.tools](https://kata.tools)

  : I developed kscript as a new programming language that is highly dynamic, with math, GUI development, app development, and performance as first class concerns

  : Check out the [web demo](https://term.kscript.org/) (try `import m; for x in range(1, 10), print(x, m.zeta(x))`) and the [documentation](https://docs.kscript.org)

<!--

2017-06 - [FractalRender (in Scratch)](https://scratch.mit.edu/projects/168228453/)

  : Yet another fractal rendering program I wrote, this time in Scratch (just for fun)

  : ![screenshot of scratch](/files/art-fractal/scratch.webp)
-->

2017-05 - [SimpleSummit / Bubbles](https://github.com/simplesummit)

  : SimpleSummit is a cluster computer made of NVIDIA Jetson hardware, used to run a realtime interactive fractal simulation

  : I was the primary software developer for the fractal application, and assisted with the physical design as well

  : ![screenshot of fractalexplorer](/files/fractalexplorer0.webp)


  : ![cluster setup](/files/simplesummit-0.webp)

2017-02 - [GNU MPFR](https://www.mpfr.org/)

  : I contributed some bug-fixes and test-cases for special functions, such as the [Beta function](https://en.wikipedia.org/wiki/Beta_function)

  : I was also active on the [GNU GMP mailing lists](https://gmplib.org/list-archives/gmp-discuss/2017-May/006108.html)

2016-10 - [EZC (programming language)](https://github.com/chemicaldevelopment/ezc)

  : An esoteric, stack-based, [RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation)-based language

2016-09 - [PGS (Prime Generator Search)](https://github.com/ChemicalDevelopment/PGS)

  : I developed this application to search polynomials (mainly quadratics) to find those which are prime for many consecutive values

  : For example, $ 36 x^2 - 810 x + 2753 $ is prime for 45 consecutive values (starting at $ 0 $) (PGS independently re-discovered this, which is the current world record for quadratic prime generators)

2016-01 - [OEIS A267263](https://oeis.org/A267263)

  : I authored an integer sequence, defined as the 'number of non-zero digits in representation of n in primorial base' (whew...). This is basically the equivalent of the [Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight), but for a mixed-radix number system based on primes

2015-09 - [Agilaire 'pilog'](https://agilaire.com/)

  : I worked as an independent contractor with Agilaire to produce a low-cost datalogger for air quality instrumentation, using a Raspberry PI

2015-08 - [L&N STEMpunks FRC #3966 team (robotics)](https://www.youtube.com/c/LNSTEMpunksorg/videos)

  : I was the leader of the programming department for 2 years, a member for 3 total years
  
<center>
<iframe width="960" height="540" src="https://www.youtube.com/embed/RBQL_KEJ_q0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

  : [Check out a match by us!](https://www.youtube.com/watch?v=gzqFjdk8j0o)

  : [some cool photos here](https://www.instagram.com/lnstempunks)

  : ![Thumbs Up](/files/cade-frc3966-thumbs0.webp){: .img-inline } ![Another Thumbs Up](/files/cade-frc3966-thumbs1.webp){: .img-inline }

2014-11 - [Bukkit/Spigot Plugins](https://dev.bukkit.org/projects/cade-gamble)

  : I authored plugins for Minecraft, in Java (some of which were for my server)
   
  : [my page on bukkit.org](https://dev.bukkit.org/members/_ForgeUser14038486/projects)

  : [my page on spigotmc.org](https://www.spigotmc.org/members/cadebrown.44717/)

