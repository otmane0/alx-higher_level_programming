#!/usr/bin/python3
"""A module for Square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a square with a specific size.

        Args:
            size (int):The size of the square (default is 0).
        """
        self.__size = size
        self.__validate_size()

    def __validate_size(self):
        """Validate the size attribute."""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
