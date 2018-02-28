#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

now = datetime.now()
delta = datetime(now.year, 12, 31, 23, 59, 59) - now

sec = delta.seconds
h = sec//3600
m = (sec//60) % 60
s = sec % 60
hous = '{:02d} {:02d} {:02d}'.format(h, m, s)

print(delta)
