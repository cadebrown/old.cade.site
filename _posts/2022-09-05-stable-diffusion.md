---
layout: post
title: "Guide to Stable Diffusion"
tags: [art, ml]
thumb: /img/screen-sd-web.png
---

[Stable Diffusion](https://stability.ai/blog/stable-diffusion-announcement), an open-source AI text-image model, was recently released. It's notable for being the first "big-boy" (i.e. high fidelity, state-of-the-art quality) model that is completely freely available. 

If you haven't already, check out my [post about DALL-E 2](/dalle2) for some background on what the heck this AI art stuff even is. If you're lookin


## Setup

### Free Demo

There's a [free demo](https://huggingface.co/spaces/stabilityai/stable-diffusion) on huggingface, which is a great way to test it out. Although it can be ran from anywhere (even mobile), it's slow since it's running on a free tier, open queue.

Good for just expirementing but not for serious work.

### Google Colab Notebook (web client)

If you don't have or want to use a GPU or hardware to run the model yourself (or you're not a nerd who can follow programming instructions), you can use the Google Colab notebook. This is a web-based client that lets you run the model in the cloud. It's free, but you'll need a Google account to use it.

There's a few different notebooks out there, and will probably be more and more made. You should google "Stable Diffusion colab notebook" if these are out of date.

  * [Stable Diffusion: txt2img, img2img, and inpainting](https://colab.research.google.com/drive/1etx3Jn4vj-OiWGF3_u2URP52VKZF4A7O?usp=sharing)


### Local: UNIX setup for lstein/stable-diffusion

If you use an Apple Silicon Mac, you can use [lstein's fork of Stable Diffusion](https://github.com/lstein/stable-diffusion), which adds support for M1/M2 macs, as well as a very cool web interface that makes prototyping easy. 

Just follow the [setup instructions](https://github.com/lstein/stable-diffusion/blob/main/docs/installation/INSTALL_MAC.md); they work as is. However, some of the scripts had problems running on my M1 macbook, so I just used the dream web interface instead:

```shell
# run the web interface
$ python3 scripts/dream.py --web
```

## Usage

In this section I'll share some tips and tricks for generating.

### Prompts

> Cyberpunk ethereal alien planet with rainbow mist auras, dense mushroom forests, canyons, and river deltas. 8k high quality digital art landscape

> Ancient caverns of existence with a 7 dimensional god meditating with a rainbow aura. 4k digital art and oil painting


## Results

Check out all my stable diffusion results [here](/art/all-stable-diffusion). Here's a sample:

{% include gallery.html filenames="/img/sd-space-0.png;/img/sd-space-1.png;/img/sd-space-2.png;/img/sd-space-3.png;/img/sd-evil-0.png;/img/sd-evil-1.png" %}


