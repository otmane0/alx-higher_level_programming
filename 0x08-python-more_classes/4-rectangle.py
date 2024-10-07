"""repr() should return a string representation of the rectangle
to be able to recreate a new instance by using eval() (see example below)
You are not allowed to import any module"""
#!/usr/bin/python3
"""A module  Rectangle"""


class Rectangle:
    """Represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize atrib"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gitter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set and raise of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Area func"""
        return self.__width * self.__height

    def perimeter(self):
        """Func for perimeter"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """String print"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = ""
            for i in range(self.__height):
                string += ("#" * self.__width)
                if i != self.__height - 1:
                    string += "\n"

            return string

    def __repr__(self):
        """Repr for eval"""

        return f"Rectangle({self.width}, {self.height})"












