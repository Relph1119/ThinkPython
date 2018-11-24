#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: is_anagram.py
@time: 2018/11/23 21:17
@desc:
"""

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

if __name__ == '__main__':
    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))