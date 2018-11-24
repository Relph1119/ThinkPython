#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: cumsum.py
@time: 2018/11/23 21:08
@desc:
"""
def cumsum(t):
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res

if __name__ == '__main__':
    t = [1, 2, 3]
    print(cumsum(t))