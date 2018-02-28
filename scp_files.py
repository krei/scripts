#! /usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
from scp import SCPClient

username = ''
password = ''
host = ''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=username, password=password)

with SCPClient(ssh.get_transport()) as scp:
    scp.get("/var/log/messages")
