# Setting up a `docker` image

Here is example material used to set up the `docker` image that creates the example figure.

## Dockerfile

The Dockerfile is key. Using `docker`, run

```
docker build -t <docker_image> .
```

(here I've been using `ianhawke/pyro:v#` with the `#` replaced by a version number).

Running through the commands in order:

```
RUN groupadd -r pyro && useradd -rmg pyro pyro
```

Some of the commands used don't like being run as root, so we add a new user.

```
RUN apt-get update && apt-get install -y python-virtualenv python-dev python-matplotlib python-numpy python-scipy git gfortran
USER pyro
WORKDIR /home/pyro
RUN git clone https://github.com/zingale/pyro2.git /home/pyro/pyro2
WORKDIR /home/pyro/pyro2
RUN git reset --hard 5abfe85b8b6683e562a535303d925935db17cabe
ENV PYTHONPATH=/home/pyro/pyro2
RUN /home/pyro/pyro2/mk.sh
```

These commands set up the container for the `pyro` code, by

1. Installing required dependencies
2. Downloading the code from `github`
3. Rewinding to a specific version
4. Setting environment variables and compiling as needed.

```
COPY inputs.smooth_novis plot_nointeract.py Makefile /home/pyro/pyro2/
USER root
RUN chown pyro:pyro inputs.smooth_novis plot_nointeract.py Makefile
RUN chmod a+x plot_nointeract.py
```

We then have to copy the input (parameter) file that runs the simulation, the plotting script, and the Makefile to produce the figures. As these are copied by `docker` as root, we then change the ownership of these files (this probably isn't needed at this point as the simulation is currently run as root).

## Parameter files

The parameter file `inputs.smooth_novis` and the plotting script `plot_nointeract.py` are minor alterations to the standard `pyro` files. The only difference is to switch off all references to interactive display, which the container doesn't have.

## Makefile

The `Makefile` contains two targets.

The first (`plot.png`) actually creates the figure by running the simulation and then running the plotting script.

The second (`figures`) is the key target required by `im2sim`. This copies the `plot.png` file to the shared volume so that we can get it outside the container. The change of ownership of the file is almost certainly not needed now.
