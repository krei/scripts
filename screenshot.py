#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyscreeze

SAVE_PATH = "/home/krei/screen"

def change_dir():
    os.chdir(SAVE_PATH)

def take_screenshot():
    filename = input("What do you want to name the screenshot? ")
    pyscreeze.screenshot(filename + ".png")

if __name__ == '__main__':
    change_dir()
    take_screenshot()
