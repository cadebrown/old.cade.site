---
layout: default
title: Links
permalink: /links
---

These are links to things I've found on the web for everything from math, programming, utilities, research, papers, and videos. This page is mainly for my reference (to keep track of everything I use regularly), but maybe it can save you some time as well.

# Applications and Tools

[pandoc: free document conversion online, no BS](https://pandoc.org/try/)

: Useful for quickly converting between markdown, HTML, $\LaTeX$, and other formats in the browser.

[WolframAlpha: computational knowledge engine (google on steroids)](https://www.wolframalpha.com/)

: Understands math, natural language, web queries and more. Seriously just ask it anything. Saves a lot of time and effort instead of having to program and google things.

[NumCalc: numerical/scientific web calculator](http://numcalc.com/)

: Useful for quick calculating when you need arbitrary precision, symbolic computation, or special functions quickly.

[Artvee: Discover Classical Art](https://artvee.com/)

: Discover classical art and navigate y artist, time period, or color palette.

[CLIP Image Retrieval: semantic image search using AI](https://rom1504.github.io/clip-retrieval/?back=https%3A%2F%2Fknn5.laion.ai&index=laion5B&useMclip=false&query=polyhedral+art+with+geometric+fractal+patterns)

: Find reference images for art or for searching for specific images that you can't remember the name of (I use it for finding [memes](https://rom1504.github.io/clip-retrieval/?back=https%3A%2F%2Fknn5.laion.ai&index=laion5B&useMclip=false&query=meme+of+a+dog+in+a+bed)).

: Also, check out this article: [Semantic search at billions scale](https://rom1504.medium.com/semantic-search-at-billions-scale-95f21695689a)

[Latent Loops: make electronic music with machine learning](https://teampieshop.github.io/latent-loops/)

: Interpolates melodies and makes new combinations of them in the browser.

[runway ML studio](https://runwayml.com/)

: Web-based video editing and content studio that uses ML models

# Informative Pages

[Feature Visualization: How neural networks build up their understanding of images](https://distill.pub/2017/feature-visualization/)

# Talks/Slides

[Polyhedral Compilation as a Design Pattern for Compiler Construction](https://pliss2019.github.io/albert_cohen_slides.pdf) 

# Programming Libraries

[PyTorch: Machine Learning Framework](https://pytorch.org/)

: Flexible and easy to use, more generalizable than Tensorflow and better for research. Includes automatic differentiation, GPU support, and a large ecosystem of libraries.

: Some extra PyTorch packages I use:
: * [PyTorch3D](https://pytorch3d.org/): 3D differentiable rendering and geometry for deep learning
: * [DEODR](https://github.com/martinResearch/DEODR): Another differentiable renderer
: * [xFormers](https://github.com/facebookresearch/xformers): PyTorch implementation of Transformer models

: And, if you're interested in "hacking" PyTorch or writing your own backend, check these out:
: * [Writing a Toy Backend Compiler for PyTorch](https://jott.live/markdown/Writing%20a%20Toy%20Backend%20Compiler%20for%20PyTorch)


[OpenCV: Computer Vision Library](https://opencv.org/)

: Bulky but comprehensive library for computer vision, uses Python bindings.

[SOD: An Embedded Computer Vision & Machine Learning Library](https://sod.pixlab.io)

: Edge computing is awesome! For IoT/embedded needs this is way easier than OpenCV.

[MAGMA: Matrix Algebra on GPU and Multicore Architectures](https://icl.utk.edu/magma/overview/index.html)

: GPU-accelerated library for linear algebra (BLAS & LAPACK) that I worked on, also includes some sparse linear algebra.

[libbf: Arbitrary Precision Floating Point Library](https://bellard.org/libbf/)

[GMP: GNU Multiple Precision Arithmetic Library](https://gmplib.org/)

: Arbitrary precision arithmetic library for C, which is very popular but not the best in my opinion.

: See also:
: * [gmpy2: Python bindings for GMP/MPFR](https://pypi.org/project/gmpy2/)
: * [MPFR: GNU Multiple Precision Floating-Point Reliable Library](https://www.mpfr.org/)
: * [MPC: GNU Multiple Precision Complex Arithmetic Library](https://www.multiprecision.org/mpc/)
:   * Also, check out all the other math libraries at [multiprecision.org](https://www.multiprecision.org/)

[FLINT: Fast Library for Number Theory](https://flintlib.org/)

: Symbolic computing library for solving/evaluating number theory problems.

[AITemplate: Efficient AI Compiler](https://github.com/facebookincubator/AITemplate)

: For example, check out how to [speed up StableDiffusion](https://github.com/facebookincubator/AITemplate/tree/main/examples/05_stable_diffusion)

[click: Python Option Parsing](https://click.palletsprojects.com/en/8.1.x/)

[youtube-dl: Download YouTube videos](https://github.com/ytdl-org/youtube-dl)

[zstd: Fast Compression Algorithm](http://facebook.github.io/zstd/)

# ML/AI Models You Can Use

These are the current "best" models for various tasks that you can actually use in some way right now.

[pharmapsyhchotic's Tools and Resources for AI Art](https://pharmapsychotic.com/tools.html)

: A great list of models, notebooks, and more for using AI to make art

[StableDiffusion: high fidelity Text-To-Image model (open source!)](https://stability.ai/blog/stable-diffusion-announcement)

: A godsend for generating art, reference images, and anything else you could want. Runs on ~4GB of VRAM and fairly fast too. Check out my [art](/art) page for some examples

: [High-Resolution Image Synthesis with Latent Diffusion Models (A.K.A. LDM & Stable Diffusion)](https://ommer-lab.com/research/latent-diffusion-models/): Website and paper that gives technical explanations

: If you're a non-programmer, or you just want a simple interface check these out:
: * [gradio: free and simple StableDiffusion web interface](https://huggingface.co/spaces/stabilityai/stable-diffusion)
: * [deforum: StableDiffusion colab notebook and resources](https://deforum.github.io/#about)

: For actually running the model, there are many forks each with their own features. Here's a short list of ones I've used:
: * [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI): overall best version, has a cool web UI, CLI REPL, and more! 
: * [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 
: * [CompVis/stable-diffusion](https://github.com/CompVis/stable-diffusion): official code, but not efficient or feature-rich

: In addition to direct implementations, also check out some projects that use StableDiffusion:

: * [jquesnelle/txt2imghd](https://github.com/jquesnelle/txt2imghd): making highquality image by upscaling and diffusion

: Outside of ML models, there are other tools that help the process of animation:

: * [MagicPrompt, for automatically generating/completing StableDiffusion prompts](https://huggingface.co/spaces/Gustavosta/MagicPrompt-Stable-Diffusion): 
: * [Keyframe string generator for AI animation notebooks](https://www.chigozie.co.uk/keyframe-string-generator/)
: * [Audio to keyframe string generator](https://www.chigozie.co.uk/audio-keyframe-generator/)

: And finally, some more related research:
: * [Textual Inversion](https://textual-inversion.github.io/)


[EbSynth](https://ebsynth.com/): 3D-aware style transfer

[DALL-E 2: Text-To-Image model API](https://openai.com/dall-e-2/)

: Now in open access with a token system, you can generate very good imagery using OpenAI's API and web interface. Good if you aren't looking to setup a ML developer environment and run StableDiffusion yourself

: [DALL-E 2: Hierarchical Text-Conditional Image Generation with CLIP Latents](https://cdn.openai.com/papers/dall-e-2.pdf): the paper from OpenAI

[VQGAN+CLIP: Text-To-Image modular architecture](https://ljvmiranda921.github.io/notebook/2021/08/11/vqgan-list/)

: A bit "old school" at this point since StableDiffusion and DALL-E 2, but VQGAN+CLIP models will always have a place in my heart for being the first to really show the power of multimodal ML art architectures. And, in my opinion, the VQGAN+CLIP models have a unique artistic style that is just not found in the more "photorealistic" models (especially for pixel art)

: [Use PyTTI-Tools if you are or aren't a programmer](https://pytti-tools.github.io/pytti-book/intro.html)

[GLM-130B: NLP Model for Text Generation](https://arxiv.org/pdf/2210.02414.pdf)

: Better than GPT-3 at most things, available in different sizes, and [free to download and use](https://github.com/THUDM/GLM-130B)

[GPT 3: NLP Model for Text Generation](https://en.wikipedia.org/wiki/GPT-3)

: State of the art in text generation, at 176 billion parameters this model is just too large to run yourself. You can run it using [OpenAI's API to GPT-3](https://openai.com/api/)

: Here's a [walkthrough of GPT architecture](https://dugas.ch/artificial_curiosity/GPT_architecture.html). This is the best overall explanation I've seen

[Real-ESRGAN: Image Super Resolution](https://github.com/xinntao/Real-ESRGAN)

: For image super resolution (just say: AI, enhance and zoom image!), this is the best deployed general solution I've seen

[RIFE: Real-Time Intermediate Flow Estimation for Video Frame Interpolation](https://github.com/megvii-research/ECCV2022-RIFE) 

: For video frame interpolation (just say: AI, increase frame rate fluidly!), this is the best downloadable model out there. This is kind of controversial because different models do different things better but I like RIFE the best

: [I use hzwer/Practical-RIFE](https://github.com/hzwer/Practical-RIFE), which promises better aesthetics and is easier to use

: [I also use nihui/rife-cnn-vulkan](https://github.com/nihui/rife-ncnn-vulkan), which runs on Apple Silicon and has a nice interface (although you'll have to use FFMPEG in addition)

[HIFIC: High-Fidelity Generative Image Compression](https://hific.github.io/)

: This model can be used to get insane results in image compression (much better than JPEG)

: [PyTorch implementation, since TensorFlow is so 2019](https://github.com/Justin-Tan/high-fidelity-generative-compression)

[AIVC: Artificial Intelligence-based Video Coding](https://github.com/Orange-OpenSource/AIVC)

: Although not as much of a upgrade as HIFIC is for images (relative to existing codecs), this is still interesting research as we wait for a superior one to emerge...

: [Check out the interactive slides](https://theoladune.github.io/AIVC-Seminar/)

[NNCP: Lossless Data Compression with Neural Networks](https://bellard.org/nncp/)

: Neural networks typically aren't easily made into lossless compressors, but this implementation gives state-of-the-art results (albeit with slow compression speed) for text compression

[Consistent Video Depth Estimation](https://roxanneluo.github.io/Consistent-Video-Depth-Estimation/)

[Magenta Colab Notebooks: ML music resources](https://magenta.tensorflow.org/demos/colab/)

[LAVIS: A one-stop library for language-vision intelligence](https://github.com/salesforce/LAVIS)

: This library can do anything from image captioning to image classification to image generation. It's great to quickly integrate into your own projects

[bRigNet: Automatic neural net 3D character rigging in Blender](https://zhan-xu.github.io/rig-net/)

: Check out the [code here: pKrime/brignet](https://github.com/pKrime/brignet)

[Deep Motion Editing: deep learning for 3D character motion](https://github.com/DeepMotionEditing/deep-motion-editing)

: Motion style transfer, retargetting, and more 3D animation features

[torch-ngp: Neural Graphics Primitives](https://github.com/ashawkey/torch-ngp)

[Awesome Neural Rendering (curated)](https://github.com/weihaox/awesome-neural-rendering)



# ML/AI Research Papers/Models

[ACT-1: Transformer for Actions](https://www.adept.ai/act)

: A very ambitious research/product that aims to create a transformer that "can do anything a human can do in front of a computer"

: This is a first of it's kind that I think will end up being the primary way we interact with computers in the future. Seriously this thing is cool AF!

[WebGPT: Improving the Factual Accuracy of Language Models through Web Browsing](https://openai.com/blog/webgpt/)

: [Interesting article about WebGPT](https://www.infoq.com/news/2022/01/openai-webgpt/), a model meant to surf the web to answer questions

[Training Compute-Optimal Large Language Models (Chinchilla), by DeepMind/Google](https://arxiv.org/abs/2203.15556)

: Chinchilla, better and smaller than GPT-3. Also, this paper has a great introduction that explains broad ideas in ML/AI. Notable for also considering compute efficiency (LLMs are getting expensive, so this is becoming more important)

[Video Diffusion Models](https://video-diffusion.github.io/)

: Soon-to-be-outdated, but an interesting paper about using diffusion models for video generation

[Infinite Nature: Perpetual View Generation of Natural Scenes from a Single Image](https://infinite-nature.github.io/)

: Basically an infinite 3D fractal zoom into landscapes, works fairly well

[Dream Fusion Paper: Text-to-3D using 2D Diffusion](https://dreamfusionpaper.github.io/)

: Interesting proof of concept of using diffusion models to generate 3D scenes from text, with no 3D data or training required! Uses optimization like DeepDreaming, unlike typical ML models which train then use inference

[Deep Positron: A Deep Neural Network Using the Posit Number System](https://arxiv.org/pdf/1812.01762.pdf)

# Datasets 

[Google Dataset Search](https://datasetsearch.research.google.com/)

[LAION-5B: A new era of open large-scale multi-modal datasets](https://laion.ai/blog/laion-5b/)

: A new large dataset, used to train Stable Diffusion, but also freely available as subsets for individuals who don't have 240TB of storage for the full dataset

: Also, has lots of good metadata on the considerations that went into it, and the challenges of creating a large dataset

[Vimeo-90k](http://etoflow.csail.mit.edu/)

: High quality dataset from Vimeo videos

[OpenWebText2, by EleutherAI](https://www.eleuther.ai/projects/owt2/)

: Large text database, generated from positive voted Reddit links

[Common Crawl dataset](https://en.wikipedia.org/wiki/Common_Crawl) - Common crawl of the entire web

[DeepVideo, with Sports-1M](https://cs.stanford.edu/people/karpathy/deepvideo/) - Sports-1M dataset, scraped from YT

# Books (Programming, Math, Philosophy)

[The Art of Computer Programming, by Donald Knuth](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming)

: Possibly the best book on computer science ever written, deals primarily with algorithms and their implementations

[Modern Computer Arithmetic, by Richard Brent and Paul Zimmerman](https://books.google.com/books/about/Modern_Computer_Arithmetic.html?id=-8wuH5AwbwMC&source=kp_book_description)

: A useful book for implementing bignum arithmetic, goes into many, many algorithms and special cases. Basically all you need to write your own MPFR/libbf/GMP library

[Advanced Programming in the Unix Environment, by Richard Stevens](https://en.wikipedia.org/wiki/Advanced_Programming_in_the_Unix_Environment)

: Heavily recommended for C programming, teaches the C standard library for UNIX OSes. I've got the physical book and it's great for perusing

[The Elements](https://en.wikipedia.org/wiki/Euclid%27s_Elements)

: Written by Euclid around 300BC, this book is a good introduction to the basics of mathematics starting with the basics of geometry

: In my opinion, this should be the first mathematics textbook for schools to use. It's ridiculous that most schools to teach students geometry without using Euclid's work. Anything to overpay the private companies that produce US textbooks, I guess...

[Prime Numbers and the Riemann Hypothesis](https://books.google.com/books/about/Prime_Numbers_and_the_Riemann_Hypothesis.html?id=jyU7rgEACAAJ)

: Very useful book, for people of all backgrounds (not just mathematicians) that explains prime numbers, number theory, and the Riemann Hypothesis. Gives multiple formulations, diagrams, and explanations. My favorite book on my favorite problem in all of mathematics (so far)!

## Papers (Math)

[On the Number of Primes Less Than a Given Magnitude](https://en.wikipedia.org/wiki/On_the_Number_of_Primes_Less_Than_a_Given_Magnitude)

: Possibly the most influential (and yet still underrated) paper in all of mathematics, I highly recommend this paper. Check out [my blog post](/2020/08/05/diy-gamma-zeta) on the Gamma/Zeta function implementations

[Counterexample To Euler's Conjecture on Sums of Like Powers](https://www.ams.org/journals/bull/1966-72-06/S0002-9904-1966-11654-3/S0002-9904-1966-11654-3.pdf)

: One of my favorite papers, although not particularly explanative. A computer-assisted dis-proof of one of Euler's conjectures

[Fast constant-time GCD computation and moular inversion](https://eprint.iacr.org/2019/266.pdf)

[Machine Learning-Aided Numerical Linear Algebra: Convolutional Neural Networks for the Efficient Preconditioner Generation](https://sc18.supercomputing.org/proceedings/workshops/workshop_files/ws_lasalss102s2-file1.pdf)

: And associated [talk/slides](https://icl.utk.edu/~hanzt/talks/ICL_nov2018.pdf)

[The FBHHRBNRSSSHK-Algorithm For Multiplication in Z_{2}^{5x5} is Still Not The End of the Story](https://arxiv.org/pdf/2210.04045.pdf)

## Papers (Programming)

[The Humble Programmer, by Edsger Dijkstra](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD03xx/EWD340.html)

: Dijkstra has almost all the correct opinions about programming... A must read!

[What Do NLP Researchers Believe? Results of the NLP Community Metasurvey](https://arxiv.org/pdf/2208.12852v1.pdf)

: It's important to at least know  what experts in the field believe about AGI, scalability, and so forth. Some takeaways are that overall, 89% say their job is "publication-oriented" (academic and industry), and the split on whether language models actually understand human language is split 50-50

[Inverse Graphics GAN: Learning to Generate 3D Shapes from Unstructured 2D Data](https://arxiv.org/pdf/2002.12674.pdf)

[Design, Optimization, and Benchmarking of Dense Linear Algebra Algorithms on AMD GPUs](https://www.icl.utk.edu/files/publications/2020/icl-utk-1405-2020.pdf)

: My paper, which discusses my work on porting and performance tuning the [MAGMA](https://icl.cs.utk.edu/magma/) library

## Papers (Programming Language Theory)

[Design Principles Behind Smalltalk, by Daniel H. H. Ingalls](https://www.cs.virginia.edu/~evans/cs655/readings/smalltalk.html)

: Smalltalk is incredibly important to understand the languages that came after it, because it was designed with a great purpose and vision. 

: **Even if you have heard about Smalltalk, READ THIS**. Unfortunately, if you just believe the common view that "Smalltalk is an object oriented language" you have fallen victim to the propaganda. The best contributions of Smalltalk are the fact that the objects send messages to each other, and that atomistic communication between objects is actually the benefit of OOP. To quote the paper: "Purpose of Language: To provide a framework for communication". 

: All OOP languages that came after but don't implement message passing are failing to realize the true benefit of OOP.

[Blub Paradox, by Paul Graham](https://wiki.c2.com/?BlubParadox)

: You can't trust the opinions of the others, because of the Blub paradox: they're satisfied with whatever language they happen to use, because it dictates the way they think about programs.

[One VM to Rule Them All](https://dl.acm.org/doi/10.1145/2509578.2509581)

: In my opinion, any modern language should be based on the VM architecture for portability and reliability. There is literally no reason to not start with that, and give specialized compilations for popular platforms. Seriously you will be kicking yourself if you don't

: Also see [GraalVM](https://www.graalvm.org/) as a case study for writing VMs

[Codata in Action](https://www.microsoft.com/en-us/research/uploads/prod/2020/01/CoDataInAction.pdf)

: My favorite explanation of how codata can actually be used. Essentially, it works as encoding control flow and order on top of normal data. I think this is something new programming languages need to use as it is lazier and easier to reason about in many cases.

: I'm surprised this came from Microsoft... One of the few times they have positively affected programming.

[GOTO Considered Harmful, by Edgar Dijkstra](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf)

: Why `goto` statements (i.e. unstructured control flow) are bad. It's so important to understand this, because even allowing low-level unstructured control flow inhibits the ability for optimizers and static analyzers to do their job. Not to mention the ability of programmers to reason about the code.

: On a meta-note, this paper established the "X considered harmful" title meme, which is still used today. 

[Structured Programming with `goto` statements, by Donald Knuth](https://pic.plover.com/knuth-GOTO.pdf)

: Great history about the `goto` debate, with a lot of interesting anecdotes and analogies to the world of mathematics. Although Knuth was probably in the wrong here (at least, in our modern view) in suggesting `goto` has valid uses, it's refreshing to hear a different perspective on the matter.

[Notation as a Tool of Thought, by Kenneth Iverson](https://www.eecg.utoronto.ca/~jzhu/csc326/readings/iverson.pdf)

: Important work by a Turing award winner that explores how notation and language can affect our thinking. So often overlooked is the fact that "ugly" or otherwise "bad" syntax is conducive to worse quality code, and conversely that "pretty" syntax can lead to better code.

: All syntaxes are not created equal! We should strive for syntaces that are easy to read and write, and that are easy to reason about.

[Algebraic Subtyping (thesis), by Stephen Dolan](https://www.cs.tufts.edu/~nr/cs257/archive/stephen-dolan/thesis.pdf)

: A long, grueling tour of algebraic subtyping, but there are a lot of good nuggets in there. Also great to get acquainted with the notation

[Cogent: uniqueness types and certifying compilation](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/47AC86F02534818B95A56FA1A283A0A6/S095679682100023Xa.pdf/cogent-uniqueness-types-and-certifying-compilation.pdf)

: Great end-to-end example about the theory of uniqueness types 

[Types, Abstraction, and Parametric Polymorphism, by John Reynolds](https://people.mpi-sws.org/~dreyer/tor/papers/reynolds.pdf)

: A great theory paper explaining distinctions between "types", "sets", and some of the problems with common conceptions we have about programming and math. A must-read for anyone making a new programming language, so as to not repeat the mistakes of the past and thinking with a mathematical mindset.

[An Expirement with Inline Substitution, Rice University](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.14.6721&rep=rep1&type=pdf)

: Results are dated, but a good example of a historical note where inlining *did not* aid in perforance. Of course, nowadays it is absolutely required due to the more abstract nature of programming

[PolyJIT: Polyhedral Optimization Just in Time](https://www.infosun.fim.uni-passau.de/publications/docs/SAGLijpp2018.pdf)

: Application of JIT techniques with polyhedral compilation

[Diesel: DSL for Linear Algebra and Neural Net Computation on GPUs](https://dl.acm.org/doi/pdf/10.1145/3211346.3211354)

: Example of a language geared at numerics-heavy compilation (focusing on neural networks). I actually ended up working with the authors of this paper as part of my NVIDIA internship

[LISP 1.5 Programmer's Manual](https://www.softwarepreservation.org/projects/LISP/book/LISP%201.5%20Programmers%20Manual.pdf)

[Structure and Interpretation of Computer Programs](https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs)

