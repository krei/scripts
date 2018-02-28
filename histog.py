#! /usr/bin/env python
# -*- coding: utf-8 -*-

def histogram(h, height, top=None, bottom=0):
    """Print histogram with `height` characters tall
    `top` and `bottom` define interval to display
    """
    # defaults
    if top is None:       top = max(h)
    if bottom is None:     bottom = 0

    # normalize data
    n = [height * (i-bottom) / (top-bottom+1) for i in h]

    # plot data
    for y in range(height-1, -1, -1):
        w = (y / height) * (top-bottom+1) + bottom
        print(''.join('#' if v > w else ' ' for v in n))


histogram(range(10), 10)
histogram([1, 10, 4, 5, 2, 3, 3, 3, 9, 1, 7], 10)
