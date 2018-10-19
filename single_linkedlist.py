#!/usr/bin/env python
# coding:utf-8

# Data Structures & Algorithms - single_linkedlist.py
# 2018/10/18 15:12

__author__ = 'Wingfai Chow <chowwingfai@gmail.com>'

class Node(object):
    # single node
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    # a single way linked list
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

    def get_head(self) -> object:
        return self.head

    def insert(self, position, data):
        if position < 0:
            print('insert error : position must be equal to or greater than 0.')
        elif position == 0 or position >= self.count_nodes():
            self.add(data)
        else:
            node = Node(data)
            prev = self.head
            count = 0
            while count < position - 1:
                count += 1
                prev = prev.next

            node.next = prev.next
            prev.next = node

    def remove_by_position(self, position):
        if position < 0 or position > self.count_nodes():
            print('remove error : position must be greater than 0 or smaller than linked list length.')
        elif position == 0:
            self.head = self.head.next
        else:
            # node = Node(data)
            count = 0
            prev = self.head
            while count < position - 1:
                count += 1
                prev = prev.next
            prev.next = prev.next.next




if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(4)
    linked_list.add(6)
    linked_list.insert(3, 10)
    linked_list.remove_by_position(1)
    node_1 = linked_list.get_head()
    while node_1:
        print(node_1.data)
        node_1 = node_1.next
    print('linked list length is ' + str(linked_list.count_nodes()))

