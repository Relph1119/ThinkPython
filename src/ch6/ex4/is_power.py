#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: is_power.py
@time: 2018/11/18 23:51
@desc:
"""

def is_power(a, b):
    if a == 0 or b == 0:
        print("Action: a or b isn't 0")
        return None
    if b == -1:
        print("Action: b isn't -1")
        return None
    if b == 1 or a/b == 1:
        return True
    return a%b == 0 and is_power(a/b, b)

if __name__ == '__main__':
    print(is_power(100, 1))
    print(is_power(81, 3))
    print(is_power(512, 2))
    print(is_power(100, 0))
    print(is_power(-1000, -1))
    # print(is_power(2, -1))
