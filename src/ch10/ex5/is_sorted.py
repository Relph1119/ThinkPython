#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: is_sorted.py
@time: 2018/11/23 21:15
@desc:
"""

def is_sorted(t):
    return t == sorted(t)

if __name__ == '__main__':
    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))