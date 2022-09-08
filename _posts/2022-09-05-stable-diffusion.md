---
layout: post
title: "Using Stable Diffusion [Apple Silicon/M1/M2]"
categories: [art]
tags: [art, ai, ml]
thumb: /img/screen-sd-web.png
---

[Stable Diffusion](https://stability.ai/blog/stable-diffusion-announcement), an open-source AI text-image model, was recently released. It's notable for being the first "big-boy" (i.e. high fidelity, state-of-the-art quality) model that is completely freely available. 

If you haven't already, check out my [post about DALL-E 2](/dalle2) for some background on what the heck this AI art stuff even is.


## Running on Apple Silicon

Instead of using the [primary repository](https://github.com/CompVis/stable-diffusion) for Stable Diffusion, we are going to use a fork: [github.com/lstein/stable-diffusion](https://github.com/lstein/stable-diffusion). We use this fork because it has a lot more features, and crucially, supports Apple Silicon.

The post thumbnail at the beginning of this blog is the web interface to the application.

The setup instructions are [located here](https://github.com/lstein/stable-diffusion/blob/main/README-Mac-MPS.md); they worked as is. However, some of the original scripts didn't work so I just used the "web" interface:

```shell
# run the web interface
$ python3 scripts/dream.py --web
```

## Results

{% include gallery.html filenames="/img/sd-space-0.png;/img/sd-space-1.png;/img/sd-space-2.png;/img/sd-space-3.png;/img/sd-evil-0.png;/img/sd-evil-1.png" %}


