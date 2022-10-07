---
layout: post
title: "StableDiffusion: AI Posters (36x24in)"
tags: [art, ml]
thumb: /img/thumb/sd-posters.webp
---

These are high quality AI-generated posters made with [StableDiffusion](/stable-diffusion) (a text-to-image model), using various prompts I've found to be aesthetically pleasing. There are some of different sizes, which are organized on this page:

  * [(36x24in)](#poster-gallery-36x24in): small-ish posters

**NOTE: for full quality, click on image, then right click to "Save As"**

## Generation

To generate them, I used the following pipeline:

  * Used StableDiffusion to generate images in the correct ratio (24x36 -> 1.5)
    * Check [/links](/links) for ways to run StableDiffusion
  * Used [ImageMagick](https://imagemagick.org/index.php) to resize to a standard size (1/4 of final size)
    * `for f in Ain/*.png; do convert $f -resize 2700x1800 Atmp/`basename $f`; done`
  * Used [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) to upscale to full 300ppi (4x to 10800x7200)
    * `for f in Atmp/*.png; do ./realesrgan-ncnn-vulkan -i $f -o Aout/`basename $f` -s4; done`
  * Used image magick again to convert to webp
    * `for f in Aout/*.png; do convert $f -quality 98 Awebp/`basename $f .png`.webp; done`

## Poster Gallery (36x24in)

{% include gallery.html prefix="/img/sd-posters-36x24/" filenames="sd-poster-36x24-3.webp;sd-poster-36x24-13.webp;sd-poster-36x24-12.webp;sd-poster-36x24-2.webp;sd-poster-36x24-9.webp;sd-poster-36x24-15.webp;sd-poster-36x24-23.webp;sd-poster-36x24-5.webp;sd-poster-36x24-19.webp;sd-poster-36x24-18.webp;sd-poster-36x24-4.webp;sd-poster-36x24-22.webp;sd-poster-36x24-14.webp;sd-poster-36x24-8.webp;sd-poster-36x24-17.webp;sd-poster-36x24-7.webp;sd-poster-36x24-21.webp;sd-poster-36x24-20.webp;sd-poster-36x24-6.webp;sd-poster-36x24-16.webp;sd-poster-36x24-1.webp;sd-poster-36x24-11.webp;sd-poster-36x24-10.webp;sd-poster-36x24-0.webp" %}
