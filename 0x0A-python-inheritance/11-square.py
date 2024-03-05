#!/usr/bin/python3
""" Module for Rectangle class """

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        """main func"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)



