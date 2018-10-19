#!/usr/bin/env python
# coding:utf-8

# Data Structures & Algorithms - dual_linkedlist.py
# 2018/10/18 15:14

__author__ = 'Wingfai Chow <chowwingfai@gmail.com>'


class Node(object):
    # single node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DualLinkedList(object):
    # a dual way linked list
    def __init__(self):
        self.head = None  # set head is none

    def count_nodes(self) ->int:
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1
        return count

    def add(self, data):  # 增加一个节点
        node = Node(data)
        # if linked list's head is None, node sets as linked list's head
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            node.prev = current

    def get_head(self) -> object:
        return self.head

    def get_tail(self) -> object:
        current = self.head
        prev = self.head.prev
        while current is not None:
            prev = current
            current = current.next
        return prev

    def insert(self, position, data):
        if position < 0:
            print('insert error : position must be equal to or greater than 0.')
        elif position == 0:
            node = Node(data)
            node.next = self.head  # 从链表左到右先操作尾端
            self.head.prev = node  # 从链表右到左先操作尾端
            self.head = node
        elif position >= self.count_nodes():
            self.add(data)
        else:
            node = Node(data)
            current = self.head
            count = 0
            while count < position - 1:
                count += 1
                current = current.next

            node.next = current.next  # 从链表左到右先操作尾端
            current.next.prev = node  # 从链表右到左先操作尾端
            current.next = node
            node.prev = current

    def remove_by_position(self, position):
        if position < 0 or position > self.count_nodes():
            print('remove error : position must be greater than 0 or smaller than linked list length.')
        elif position == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            count = 0
            current = self.head
            while count < position - 1:
                count += 1
                current = current.next
            current.next = current.next.next
            current.next.prev = current


if __name__ == '__main__':
    linked_list = DualLinkedList()
    linked_list.add(1)
    linked_list.add(4)
    linked_list.add(6)
    linked_list.add(8)
    linked_list.insert(3, 10)
    linked_list.remove_by_position(1)
    node_1 = linked_list.get_head()
    while node_1:
        print(node_1.data)
        node_1 = node_1.next
    print('linked list length is ' + str(linked_list.count_nodes()))
    node_2 = linked_list.get_tail()
    while node_2:
        print(node_2.data)
        node_2 = node_2.prev
    print('linked list length is ' + str(linked_list.count_nodes()))
