#!/usr/bin/env python
# coding:utf-8

# Data_Structures_and_Algorithms - quick_sort.py
# 2018/10/25 11:38

__author__ = 'Wingfai Chow <chowwingfai@gmail.com>'

from random import randint


def create_array(size=10, max_num=50):
    return [randint(0, max_num) for _ in range(size)]  # 随机生成10个数


def partition(array, low_index, high_index):
    divider = low_index
    pivot = high_index
    for i in range(low_index, high_index):
        if array[i] <= array[pivot]:
            array[divider], array[i] = array[i], array[divider]
            divider += 1
        else:
            pass
    array[divider], array[pivot] = array[pivot], array[divider]
    return divider


def quick_sort(array, low_index=0, high_index=None):
    if high_index is None:
        high_index = len(array) - 1
    else:
        pass
    if low_index < high_index:
        p = partition(array, low_index, high_index)
        quick_sort(array, low_index, p - 1)  # sort lower half
        quick_sort(array, p + 1, high_index)  # sort upper half
    else:
        pass
    return array


if __name__ == '__main__':
    list_1 = [5, 4, 3, 2, 1]
    quick_sort(list_1)
