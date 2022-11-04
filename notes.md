---
layout: default
title: Notes
permalink: /notes
---

These are my personal notes on random things I'm working on, mainly meant for my own reference and to collect links, write down observations, etc.

# 2022-11-02

## Meeting: Feiyi Wang

  * He's in charge of the AI methods and analytics at scale, running on the supercomputers
  * Research directions:
    * Operational data analytics
    * Community interest
    * Intellectual value
    * AI for science: 
  * SC21 best paper award with his group, SC22 paper coming up
  * Career ladders at ORNL
    * RP: Research Professional, publications/research
    * TP: Technical professional, engineering/infrastucture

## SSNN



# 2022-10-27

## ReactNative and Expo

I was trying to set up ReactNative, and find guides for the other team members of my school project  Interguage.

  * [Expo: install](https://docs.expo.dev/get-started/installation/)

## SSNN

Today I was researching into transformer architectures, both the building blocks and extensions for efficiency purposes. It's part of a research project I'm working on [SSNN](https://github.com/cadebrown/ssnn), which is to build more efficient transformer models and find out how they scale compute-wise.

These were useful to read:

  * [Illustrated Transformer (website)](https://jalammar.github.io/illustrated-transformer/)
  * [Tensor2Tensor (notebook)](https://colab.research.google.com/github/tensorflow/tensor2tensor/blob/master/tensor2tensor/notebooks/hello_t2t.ipynb): cool interactive explorer that shows dependencies between tokens
  * [CvT: Introducing Convolutions to Vision Transformers](https://arxiv.org/pdf/2103.15808.pdf)

Steps I need to take to make progress on this project:

  * Establish a benchmark/standard to compare new architectures against
    * Compute vs time budget, or epochs? Also consider memory
    * Compare against standard transformer models (from xformers, huggingface, nn.Transformer, etc)
  * Implement new attention mechanisms, based on sparse attention. Ideas so far:
    * Use Strassen-like decompositions for faster matrix multiplication
    * Use sparse attention patterns in the matrices ($W_k$, $W_q$, $W_v$, and the feed-forward-network of each head)





