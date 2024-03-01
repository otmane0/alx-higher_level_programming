#!/usr/bin/python3
"""Define an empty class Rectangle."""


class Rectangle:

    """REpresent a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Represent a rectangle."""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        size_area = self.__width * self.__height
        return size_area

    def perimeter(self):
        return 2 * (self.__width + self.__height) if self.__width and self.__height else 0

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([self.print_symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


