#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys


def usage():
    print("Usage: " + sys.argv[0] + " <on|off|scan|disconnect>")
    print("Connect network `nmcli dev wifi connect <name> password <password>`")
    sys.exit(1)

if len(sys.argv) < 2:
    usage()

opt = sys.argv[1]

if opt == "on":
    cmd = "nmcli r wifi on"
elif opt == "off":
    cmd = "nmcli r wifi off"
elif opt == "scan":
    cmd = "nmcli dev wifi list"
elif opt == "disconnect":
    cmd = "nmcli dev disconnect wlp2s0"
else:
    usage()

subprocess.call(cmd, shell=True)
