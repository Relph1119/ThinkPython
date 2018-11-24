#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: nested_sum.py
@time: 2018/11/23 21:06
@desc:
"""

def nested_sum(t):
    total = 0
    for nested in t:
        total += sum(nested)
    return total

if __name__ == '__main__':
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))