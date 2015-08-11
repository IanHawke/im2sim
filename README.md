# im2sim

Reproducible simulation from images.

## Motivation

A simulation might be a complicated mess of dependencies, the data prodcued depends on the architecture and parameter files, and the paper that results depends on the analysis and personal whim. But often what sticks - what *becomes* the simulation - is a single plot.

This is a real problem, as that image, plot or figure can easily become detached from the data that produced it. The (wonderful) idea of reproducible computation becomes problematic if you're relying on a figure from a talk that the speaker found from Google image search...

So, as a quick hack, here is `im2sim`: a way of embedding metadata directly into the figure so that *directly from the image* the whole simulation can be reprodcued.

## Method

As a quick hack, we're going to rely on [docker](docker.com) for the reproducibility, and essentially embed links to containers directly.

## Current status

This should work

* when run using boot2docker (Mac OS)
* when run on png files
* when using the specific container for the pyro code that I've used to create the figure in the example_figure directory.

I don't think it would be at all difficult to remove any of these restrictions, but this is enough for proof-of-principle.
