#! /usr/bin/env python2
# -*- coding: utf-8 -*-

from sys import *

arg = lambda : (len(argv) > 1 and int(argv[1])) or int(input("число?: "))
factorial = lambda x: ((x == 1) and 1) or x * factorial(x - 1)
n = arg()
m = getrecursionlimit()

if n >= m :
    print("глубина рекурсии превышает установленную в системе %d, переустановлено в %d " %(m, n + 1))
setrecursionlimit(n + 1)
print("n=%d => n!=%d" % (n, factorial(n)))

if getrecursionlimit() > m :
    print("глубина рекурсии восстановлена в %d" % m)
setrecursionlimit(m)
