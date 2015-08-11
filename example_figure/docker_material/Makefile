plot.png: pyro.py
	./pyro.py advection smooth inputs.smooth_novis
	./plot_nointeract.py advection smooth_0040.pyro

figures: plot.png
	cp plot.png /figures/
	chown pyro:pyro /figures/*
