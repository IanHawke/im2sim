#!/usr/bin/env python

import matplotlib
matplotlib.use('Agg')

import plot

import numpy
import pylab
import sys
import getopt

import mesh.patch as patch

if __name__== "__main__":

    try: opts, next = getopt.getopt(sys.argv[1:], "o:h:W:H:")
    except getopt.GetoptError:
        sys.exit("invalid calling sequence")

    outfile = "plot.png"

    W = 8.0
    H = 4.5

    for o, a in opts:
        if o == "-h": usage()
        if o == "-o": outfile = a
        if o == "-W": W = float(a)
        if o == "-H": H = float(a)

    try: solver = next[0]
    except: plot.usage()

    try: file = next[1]
    except: plot.usage()

    myg, myd = patch.read(file)

    plot.makeplot(myd, solver, outfile, W, H)
