#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: test.py
@time: 2018/11/23 21:52
@desc:
"""

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

h = histogram('brontosaurus')
print(h)