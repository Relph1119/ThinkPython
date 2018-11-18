#!/usr/bin/env python
# encoding: utf-8
'''
@author: HuRuiFeng
@file: ackermann.py
@time: 2018/11/18 23:45
@desc:
'''

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


print(ackermann(3, 4))