#!/usr/bin/env python
# coding:utf-8

# Data Structures & Algorithms - recursion.py
# 2018/10/18 15:13

__author__ = 'Wingfai Chow <chowwingfai@gmail.com>'


def factorial(n: int):
    # n! = 1*2*3* ...* n!
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


def fn(n: int):
    # 1 1 2 3 5 8
    if n > 2:
        return fn(n - 1) + fn(n - 2)
    else:
        return 1


print(factorial(5))

print(fn(8))