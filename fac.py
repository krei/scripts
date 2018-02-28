#! /usr/bin/env python
# -*- coding: utf-8 -*-

n = input("Факториал числа ")
n = int(n)
factorial = 1
i = 0
while i < n:
     i = i + 1
     factorial = factorial * i
print("равен ", factorial)
