#! /usr/bin/env python
# -*- coding: utf-8 -*-

decimals = int(input("Введите натуральное число: "))
binars = ""

while decimals > 0:
    y = str(decimals % 2)
    binars = y + binars
    decimals = int(decimals / 2)

print(binars)
