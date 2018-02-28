#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

f = open(r'C:\Users\1\Desktop\testingsite.txt')
z = [lines.strip() for lines in f.readlines()]
for hostname in z:
    response = os.system("ping " + hostname)
    if response == 0:
        print(hostname, '       Is Up!       ')
    else:
        print(hostname, '       Is Down!      ')
