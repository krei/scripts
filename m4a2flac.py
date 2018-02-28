#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import subprocess

__author__ = 'krei'
__version__ = '0.0.4'
__license__ = 'Apache License. Version 2.0'
__copyright__ = 'Copyright (c) 2018, Krei'

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


for root, dirs, files in os.walk("/home/user/Музыка/"):
    for file in files:
        if file.endswith(".m4a"):
            print("Путь к файлу  " + os.path.join(root, file))

            command = ['ffmpeg']
            command.append('-i')
            command.append(file)
            command.append('-f')
            command.append('flac')
            command.append(file + '.flac')

            with cd(root):
                print(command)
                subprocess.call(command)
            print("==========================================================")
