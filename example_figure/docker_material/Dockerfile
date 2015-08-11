FROM ubuntu:14.04
MAINTAINER Ian Hawke <dr.ian.hawke@gmail.com>

RUN groupadd -r pyro && useradd -rmg pyro pyro
RUN apt-get update && apt-get install -y python-virtualenv python-dev python-matplotlib python-numpy python-scipy git gfortran
USER pyro
WORKDIR /home/pyro
RUN git clone https://github.com/zingale/pyro2.git /home/pyro/pyro2
WORKDIR /home/pyro/pyro2
RUN git reset --hard 5abfe85b8b6683e562a535303d925935db17cabe
ENV PYTHONPATH=/home/pyro/pyro2
RUN /home/pyro/pyro2/mk.sh
COPY inputs.smooth_novis plot_nointeract.py Makefile /home/pyro/pyro2/
USER root
RUN chown pyro:pyro inputs.smooth_novis plot_nointeract.py Makefile
RUN chmod a+x plot_nointeract.py
#USER pyro
