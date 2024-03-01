#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        return (2 * (self.__width + self.__height)
                if self.__width and self.__height else 0)

    def __str__(self):
        """Return the string representation of the Rectangle."""
        if not self.__width or not self.__height:
            return ""
        return '\n'.join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """Return the representation of the Rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when a Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @classmethod
    def bigger_or_equal(cls, rect_1, rect_2):
        """Return the bigger rectangle based on the area."""
        if not isinstance(rect_1, cls):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, cls):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)
