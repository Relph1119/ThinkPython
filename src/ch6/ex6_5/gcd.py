#!/usr/bin/env python
# encoding: utf-8
'''
@author: HuRuiFeng
@file: gcd.py
@time: 2018/11/19 0:16
@desc:
'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(312, 512))
print(gcd(0, 512))
print(gcd(312, 0))