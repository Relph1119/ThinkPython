#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: __init__.py.py
@time: 2018/11/22 23:41
@desc:
"""
import os, sys

def has_no_e(word):
    return word.count('e') == 0

fin = open(os.path.dirname(sys.path[2]) + os.sep + "resource"+ os.sep +"words.txt")
total = 0
no_e_count = 0
for line in fin:
    total += 1
    word = line.strip()
    if has_no_e(word):
        no_e_count += 1
        print(word)

print("Percentage of such words in the whole vocabulary :" + str(int(no_e_count/total*100)) + "%")

