#!/usr/bin/python3
"""Define an empty class Rectangle."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Represent a rectangle."""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Represent a height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Represent a height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Represent a width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Represent a width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value




