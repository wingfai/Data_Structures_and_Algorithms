#!/usr/bin/env python
# coding:utf-8

# Data_Structures_and_Algorithms - sort.py
# 2018/10/19 9:38

__author__ = 'Wingfai Chow <chowwingfai@gmail.com>'

import datetime

list_1 = [20, 3, 15, 2, 4, 10, 7, 5]
list_2 = [1, 2, 3, 4, 5]
list_3 = [5, 4, 3, 2, 1]
list_4 = [2, 1, 3, 4, 5]


def delta_time(origin_func):
    def wrapper(*args, **kwargs):
        t = datetime.datetime.today()
        func = origin_func(*args, **kwargs)
        delta = datetime.datetime.today() - t
        print(f'所需时间为 {delta}')
        return func
    return wrapper


@delta_time
def bubble_sort(sort_list: list): # 冒泡排序
    length = len(sort_list)
    if length <= 1:
        return sort_list
    else:
        for i in range(0, length):
            flag = False  # end the loop early 提前退出循环标志
            for j in range(0, length - i - 1):
                if sort_list[j] > sort_list[j + 1]:
                    sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]  # 数据交换
                    flag = True  # 表示有数据交换
                else:
                    pass
            if not flag:  # 没有进入循环，直接退出
                break
        return sort_list


@delta_time
def insert_sort(sort_list: list): # 插入排序
    length = len(sort_list)
    if length <= 1:
        return sort_list
    else:
        for i in range(1, length):
            for j in range(i, 0, -1):
                if sort_list[j - 1] > sort_list[j]:
                    sort_list[j - 1], sort_list[j] = sort_list[j], sort_list[j - 1]
                else:
                    break  # 跳出循环
        return sort_list


@delta_time
def selection_sort(sort_list: list):  # 选择排序
    length = len(sort_list)
    for i in range(0, length):
        min_number_tag = i
        for j in range(i + 1, length):
            if sort_list[min_number_tag] > sort_list[j]:
                min_number_tag = j
            else:
                pass
        sort_list[min_number_tag], sort_list[i] = sort_list[i], sort_list[min_number_tag]
    return sort_list


if __name__ == '__main__':
    print(bubble_sort(list_1))
    print(insert_sort(list_1))
    print(selection_sort(list_1))
