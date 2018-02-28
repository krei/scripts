#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

def dating(start, stop, step):
    while start < stop:
        yield start
        start += step

for d in dating(datetime(2017, 1, 2), datetime(2017, 1, 11), timedelta(hours=4)):
    print(d)
