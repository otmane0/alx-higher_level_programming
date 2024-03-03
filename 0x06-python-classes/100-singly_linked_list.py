#!/usr/bin/python3

class Node:
    """class node"""
    def __init__(self, data, next_node=None):
        """class node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """class node"""
        return self.__data

    @data.setter
    def data(self, value):
        """class node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """class node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """class node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class list"""
    def __init__(self):
        """ list"""
        self.__head = None

    def sorted_insert(self, value):
        """list"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """list"""

        values = []
        temp = self.__head
        while temp:
            values.append(str(temp.data))
            temp = temp.next_node
        return '\n'.join(values)
