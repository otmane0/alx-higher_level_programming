#!/usr/bin/python3
"""Everything is object"""

class Square:
    """Area of a square"""

    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """print def"""
        return self.__size * self.__size

    @property
    def size(self):
        """print def"""
        return self.__size

    @size.setter
    def size(self, value):
        """print def"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print def"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#",end="")
                print()

