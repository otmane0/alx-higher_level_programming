#!/usr/bin/python3
"""A module for Square"""

class Square:
    """
    Access and update private attribute
    """
    def __init__(self, size=0) :
        self.__size = size

    def area(self):
        """
        Access and update private attribute
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Access and update private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Access and update private attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("\n")
        else:
            i=0
            j=0
            for i in range (self.__size):
                print("#" * self.__size)
