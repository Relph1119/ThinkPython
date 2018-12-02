#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: print_words_more20.py
@time: 2018/11/22 23:30
@desc:
"""
import os, sys
fin = open(os.path.dirname(sys.path[2]) + os.sep + "resource"+ os.sep +"words.txt")
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)