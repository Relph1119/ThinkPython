#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: squart_root.py
@time: 2018/11/22 21:44
@desc:
"""

import math

epsilon = 0.000000000000000001

def square_root(a, x):
    while True:
        y = (x + a/x)/2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

def test_square_root(a, x):
    my_ans = square_root(a, x)
    math_ans = math.sqrt(a)
    diff = abs(my_ans - math_ans)
    print(str(a)+" "*(7-len(str(a)))+str(my_ans)+" "*(23-len(str(my_ans)))+\
          str(math_ans)+" "*(22-len(str(math_ans))), diff)

if __name__ == '__main__':
    print("a"+" "*6+"mysqrt(a)"+" "*14+"math.sqrt(a)"+" "*11+"diff")
    print("-"+" "*6+"---------"+" "*14+"------------"+" "*11+"----")

    test_square_root(1.0, 1)
    test_square_root(2.0, 2)
    test_square_root(3.0, 2)
    test_square_root(4.0, 2)
    test_square_root(5.0, 2)
    test_square_root(6.0, 2)
    test_square_root(7.0, 2)
    test_square_root(8.0, 2)
    test_square_root(9.0 ,2)
