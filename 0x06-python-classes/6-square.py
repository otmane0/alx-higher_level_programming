#!/usr/bin/python3
"""A module for Square"""

class Square:
    """
    Access and update private attribute
    """
    def __init__(self, size=0, position=(0, 0)) :
        self.__size = size
        self.position = position

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
    @property
    def position(self):
        """
        Return position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or not all(isinstance(i , int) for i in value) or len(value) != 2\
                or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
