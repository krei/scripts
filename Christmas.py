#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(-8 * np.pi, 8 * np.pi, 200)
z = np.linspace(-3, 0, 200)
r = 5
x = r * np.sin(theta)*z
y = r * np.cos(theta)*z

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(15, 0)
ax._axis3don = False

ax.plot(x, y, z,
        c='green', linewidth=2.5)

ax.scatter(0, 0, 0.2,
           c='red', s=250, marker='*')

ax.set_title(u"С новым годом!")

plt.show()
