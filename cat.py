#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

__author__ = 'krei'
__version__ = '0.0.4'


def find_files(catalog, f):
    find_files = []
    for root, dirs, files in os.walk(catalog):
        find_files += [os.path.join(root, name) for name in files if name == f]
    return find_files

print(find_files(sys.argv[1], sys.argv[2]))
