#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import math

def mandelbrot(z, c, n=50):
    for a in range(1, n):
        z = z ** 2 + c
        if abs(z) > 2:
            return z
    return 0
print("\n".join(["".join(["*" if not mandelbrot(0, x + y * 1j)
else " "
    for x in [a * 0.05 for a in range(-40, 20)]])
        for y in [a * -0.05 for a in range(-20, 20)]])
    )
