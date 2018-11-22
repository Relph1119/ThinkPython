#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: eval_loop.py
@time: 2018/11/22 22:17
@desc:
"""

def eval_loop():
    ans = ''
    while True:
        print('Please enter your words:\n')
        word = input()
        if word == 'done':
            return ans
        ans = eval(word)
        print(ans)


print(eval_loop())