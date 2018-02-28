#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__author__ = 'krei'
__version__ = '0.0.4'

hostname = "127.0.0.1"
response = os.system("ping -c 1 " + hostname)
hostname2 = "10.0.1.12"
response2 = os.system("ping -c 1 " + hostname2)
subj2 = ''
subj1 = ''

if response ==0:
    print(hostname, 'is up!')
    text1 = '127.0.0.1 is up\n'
    subj1 = 'server says OK '
else:
    print(hostname, 'is down!')
    text1 = '127.0.0.1 is down\n'
    subj1 = 'server says ALLERT '
if response2 ==0:
    print(hostname2, 'is up!')
    text2 = '10.0.1.12 is up'
    subj2 = 'server says OK'
else:
    print(hostname2, 'is down!')
    text2 = '10.0.1.12 is down'
    subj2 = 'server says ALLERT'

me = 'email@mail.ru'
you = 'email@mail.ru'
text = text1 + text2
subj = subj2 + subj1
server = "smtp.mail.ru"
port = 625
user_name = "email@mail.ru"
user_passwd = "password"
msg = MIMEText(text, "", "utf-8")
msg['Subject'] = subj
msg['From'] = me
msg['To'] = you
s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.ehlo()
s.login(user_name, user_passwd)
s.sendmail(me, you, msg.as_string())
s.quit()
