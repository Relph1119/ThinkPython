#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: middle.py
@time: 2018/11/23 21:09
@desc:
"""

def middle(t):
    return t[1:-1]

if __name__ == '__main__':
    t = [1, 2, 3, 4]
    print(middle(t))