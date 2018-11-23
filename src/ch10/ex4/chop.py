#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: chop.py
@time: 2018/11/23 21:13
@desc:
"""

def chop(t):
    del t[-1]
    del t[0]

t = [1, 2, 3, 4]
chop(t)
print(t)