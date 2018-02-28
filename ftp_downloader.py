#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from ftplib import FTP

URL = "your_ftp_server_url or IP"
username = ''
password = ''
filename = 'log.txt'

file = open(filename, 'wb')

with FTP(URL, username, email) as ftp:
    ftp.login(username, password)
    ftp.retrbinary('RETR %s' % filename, file.write)

file.close()
