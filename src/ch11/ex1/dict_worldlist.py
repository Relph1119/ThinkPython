#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: flyweight.py
@time: 2018/11/24 22:24
@desc: 享元模式
"""
import os, sys, time

def make_word_list():
    word_list = []
    fin = open(os.path.dirname(sys.path[2]) + os.sep + "resource"+ os.sep +"words.txt")
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

def in_bisect_cheat(word):
    import bisect
    word_list = make_word_list()

    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word

def in_wordlist(word):
    word_list = make_word_list()
    if word in word_list:
        return True
    return False

def dict_wordlist(search_word):
    word_list = dict()
    fin = open(os.path.dirname(sys.path[2]) + os.sep + "resource" + os.sep + "words.txt")
    for line in fin:
        word = line.strip()
        word_list[word] = 0
    if search_word in word_list:
        return True
    return False

if __name__ == '__main__':

    word = "consign"

    start_time = time.time()
    t = in_wordlist(word)
    elapsed_time = time.time() - start_time

    print("in_wordlist: " + str(t))
    print(elapsed_time, 'seconds')

    start_time = time.time()
    t = in_bisect_cheat(word)
    elapsed_time = time.time() - start_time

    print("in_bisect_cheat: " + str(t))
    print(elapsed_time, 'seconds')

    start_time = time.time()
    t = dict_wordlist(word)
    elapsed_time = time.time() - start_time

    print("dict_wordlist: " + str(t))
    print(elapsed_time, 'seconds')