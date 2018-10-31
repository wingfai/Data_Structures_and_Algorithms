#!/usr/bin/env python
# coding:utf-8

# Data_Structures_and_Algorithms - binary_search.py
# 2018/10/31 10:22

__author__ = 'Wingfai Chow <chowwingfai@gmail.com>'


def binary_search_first_value(array: list, value: int or str) -> int or str or bool:
    # binary search the first value in a list with repeat value
    low_index = 0
    high_index = len(array) - 1
    while low_index <= high_index:
        middle_index = (low_index + high_index) >> 1  # 位运算
        if array[middle_index] >= value:
            if middle_index == low_index or array[middle_index - 1] != value:
                return middle_index
            else:
                high_index = middle_index - 1
        else:
            low_index = middle_index + 1


def binary_search_last_value(array: list, value: int or str) -> int or str or bool:
    # binary search the last value in a list with repeat value
    low_index = 0
    high_index = len(array) - 1
    while low_index <= high_index:
        middle_index = (low_index + high_index) >> 1  # 位运算
        if array[middle_index] >= value:
            if middle_index == high_index or array[middle_index + 1] != value:
                return middle_index
            else:
                high_index = middle_index - 1
        else:
            low_index = middle_index + 1


def binary_search_0(array: list, value: int or str) -> int or str or bool:
    # binary search the equal or greater than value.
    low_index = 0
    high_index = len(array) - 1
    while low_index <= high_index:
        middle_index = (low_index + high_index) >> 1  # 位运算
        if array[middle_index] >= value:
            if middle_index == low_index or array[middle_index - 1] < value:
                return middle_index
            else:
                high_index = middle_index - 1
        else:
            low_index = middle_index + 1


def binary_search_1(array: list, value: int or str) -> int or str or bool:
    # binary search the equal or smaller than value.
    low_index = 0
    high_index = len(array) - 1
    while low_index <= high_index:
        middle_index = (low_index + high_index) >> 1  # 位运算
        if array[middle_index] <= value:
            if middle_index == high_index or array[middle_index + 1] > value:
                return middle_index
            else:
                low_index = middle_index + 1
        else:
            high_index = middle_index - 1


if __name__ == '__main__':
    test_list = [1, 3, 4, 5, 6, 7, 7, 7, 9, 10]
    print(binary_search_first_value(test_list, 7))
    print(binary_search_last_value(test_list, 7))
    print(binary_search_0(test_list, 2))
    print(binary_search_1(test_list, 2))