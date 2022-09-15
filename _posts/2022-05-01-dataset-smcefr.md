---
layout: post
title: "SMCEFR Dataset (Data Challenge)"
tags: [code, data, ml]
thumb: /files/smcefr/miniset.jpg
---

I was asked to sponsor a dataset for [ORNL's Smoky Mountain Conference](https://smc-datachallenge.ornl.gov/), in addition to posing a number of challenge questions. Then, researchers of all levels (undergrad to post-grad and beyond) were invited to investigate the dataset and write papers about their findings.

In order to do that, I chose to collect and process data from [the Sentinel-3 satellite missions](https://en.wikipedia.org/wiki/Sentinel-3), which is basically a bird's eye view of the Earth from space. The data is freely available, and I wrote a script to download it and process it into a format that is easy to work with. You can see the source code here: [cadebrown/smcefr](https://github.com/cadebrown/smcefr)

You can see the full dataset description and problems here: [cade.site/smcefr](https://cade.site/smcefr). TL;DR:

  * Data Source
    * Data from the Ocean Land and Color Instrument (OLCI) on the Sentinel-3 was queried.
    * Data was considered from the [OLCI’s Earth Full Resolution (EFR) data product](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-3-olci/level-1/fr-or-rr-toa-radiances)
    * All images are center-cropped to the exact 1024x1024 resolution, or were discarded if only a smaller image was available. This naturally avoided the need for normalization and resizing.
    * The images with the most extreme cases of sparsity or low-entropy were discarded. For example, images that are completely white or blue which represented dense cloud cover or ocean water, respectively.
  * Challenge Questions
    1. What methods can be used to segment and identify the regions of the images that are partially or completely obstructed by the cloud cover?
    2. Consider a case where the sensor data is incomplete, of varied quality, or totally degraded. Is there any way to take partially damaged/noisy data, and reconstruct something “closer” to the original sensor reading?
    3. To preserve data integrity, the dataset is provided as PNG, in the lossless data compression format mode. However, for a variety of purposes, it would be useful to allow a small amount of error in exchange for an appreciatiable size reduction. What can research methods be used to save space while keeping the best quality possible?

I am also a reviewer and judge for the papers, so I will be reading and grading them. 

TODO: update this post with results.

