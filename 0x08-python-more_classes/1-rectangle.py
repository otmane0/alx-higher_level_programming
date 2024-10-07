#!/usr/bin/python3
"""A module  Rectangle"""


class Rectangle:
    """Represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize atrib"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gitter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set and raise of width"""
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height< 0:
            raise ValueError("height must be >= 0")

