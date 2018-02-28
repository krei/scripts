#! /usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from decimal import *

def digest(number):
    number = bytearray('{}'.format(number), encoding='utf-8')
    h = hashlib.md5(number)
    return h.hexdigest()


def main():
    file = open('md5.txt', 'w')
    range = Decimal('0.0000000001')
    min = Decimal('0.9300000000')
    max = Decimal('0.9300000009')
    while min != max:
        file.write('{1}\n'.format(min, digest('{0:.10f}'.format(min))))
        min += range
    file.close()


if __name__ == "__main__":
    main()
