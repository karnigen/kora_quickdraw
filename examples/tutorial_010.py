#!/usr/bin/env python3

from kora_quickdraw import *
import numpy as np

x = np.linspace(-np.pi , np.pi)
y1 = np.sin(x)
y2 = np.cos(x)

# fig, ax1, ax2 = start_plot2(ax2=None)
fig, ax1, ax2 = start_plot2()
ax1.plot(x,y1)
ax1.plot(x,y2)
if ax2 is not None:
    ax2.plot(x, y1*y2)
show_plot2(1, fig, ax1, ax2, t1="sin(x) and cos(x)", t2="sin(x) x cos(x)", y2='y')




