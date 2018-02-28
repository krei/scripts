#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import getpass
import sys
import telnetlib
import time

COMMAND = sys.argv[1]
Uname = raw_input("Username:")
Pass = getpass.getpass()

DevIP = ['10.254.58.3', '10.254.58.4', '10.254.58.10']

for IP in DevIP:
    print "Connection to device %s" %IP
    t=telnetlib.Telnet(IP)
    t.read_until("Username: ")
    t.write(Uname + "\n")

    t.read_until("Password: ")
    t.write(Pass + "\n")

    t.write("terminal length 0\n")
# выводит комманду пользователя: пример написания данного атрибута "sh ip int br"
    t.write(COMMAND + '\n')

    time.sleep(1)

    output = t.read_very_eager()
    print output
