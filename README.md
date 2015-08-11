# im2sim

Reproducible simulation from images.

## Motivation

A simulation might be a complicated mess of dependencies, the data prodcued depends on the architecture and parameter files, and the paper that results depends on the analysis and personal whim. But often what sticks - what *becomes* the simulation - is a single plot.

This is a real problem, as that image, plot or figure can easily become detached from the data that produced it. The (wonderful) idea of reproducible computation becomes problematic if you're relying on a figure from a talk that the speaker found from Google image search...

So, as a quick hack, here is `im2sim`: a way of embedding metadata directly into the figure so that *directly from the image* the whole simulation can be replicated.

## Method

As a quick hack, we're going to rely on [docker](docker.com) for the reproducibility, and essentially embed links to containers directly.

## Current status

This should work

* when run using boot2docker (Mac OS)
* when run on png files
* when using the specific container for the pyro code that I've used to create the figure in the example_figure directory.

I don't think it would be at all difficult to remove any of these restrictions, but this is enough for proof-of-principle.

# Usage

## Replicating a simulation given a figure

Assuming you have `docker` installed, and that you're currently connected to the virtual machine (eg, are running in the terminal launched by `boot2docker`). Then run

```
python im2sim.py pull <figure>.png
```

This will download a `docker` image containing the code required to replicate the image, and print to screen the `<docker_image>` name. You can then use the standard interactive shell via

```
docker run -ti <docker_image> /bin/bash
```

to inspect the code. The commands run to produce the figure will be given in the `Makefile` (see below for more details).

## Preparing the images given a simulation code

You need to package your simulation code using `docker` in a very specific fashion. The `<docker_image>` must have an `ENTRYPOINT` specified. At that `ENTRYPOINT` there should be a `Makefile`. The key target for `make` is `figures`: this must exist and be runnable. This should produce the figures that you want tagged, and should copy them to the `/figures/` directory (which will be mounted by `docker` - you should assume it will exist). Finally, you *must* `push` your `<docker_image>` to `hub.docker.com` (or any other online location that a `docker pull` command can locate).

With your `<docker_image>` set up in this fashion, and again working in a terminal connected to the `docker` virtual machine (eg via `boot2docker`), run

```
python im2sim.py tag <docker_image>
```

This will create a directory `$PWD/figures` containing the figures (which currently must be `.png` files), each of which will have metadata suitable for use with `im2sim.py`. You can then use and distribute these image files and use `im2sim.py` to recover the docker image in the future.
