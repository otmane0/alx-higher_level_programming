#!/usr/bin/python3
"""A module for implementing a singly linked list."""

class Node:
    """A class representing a node in a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a node with data and a reference to the next node."""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter for the node's data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the node's data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next node."""
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """A class representing a singly linked list."""
    def __init__(self):
        """Initialize an empty linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node into the list in sorted order."""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
                new_node.next_node = temp.next_node
                temp.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
