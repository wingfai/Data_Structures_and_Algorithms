#!/usr/bin/env python
# coding:utf-8

# Data_Structures_and_Algorithms - merge_sort.py
# 2018/10/24 14:12

__author__ = 'Wingfai Chow <chowwingfai@gmail.com>'


def merge_sort(array: list):
    if len(array) <= 1:
        return array
    else:
        pass
    midpoint = int(len(array) / 2)
    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_pointer = 0
    right_pointer = 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result


if __name__ == '__main__':
    array_1 = [1, 2, 3, 4, 5, 1]
    print(merge_sort(array_1))
