#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import glob
import os

os.system("rm Tracks.mps")

fs = glob("*.mps")
s = ""
for fname in fs:
    s = s + " -f " + "\"" + fname + "\""
    print("found file %s" %fname)

fs = "gpsbabel -w -i mapsource" + s + " -o gpx -F Tracks.gpx"
print(fs)
os.system(fs);

fs = "gpsbabel -t -i mapsource" + s + " -o mapsource -F Tracks.mps"
print(fs)
os.system(fs);
