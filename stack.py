#!/usr/bin/env python
# coding:utf-8

# Data Structures & Algorithms - stack.py
# 2018/10/18 15:13

__author__ = 'Wingfai Chow <chowwingfai@gmail.com>'


class Stack(object):

    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def get_stack(self):
        return self.item


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.pop()
    print(s.get_stack())