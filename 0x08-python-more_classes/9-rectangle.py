
#!/usr/bin/python3
"""A module  Rectangle"""


class Rectangle:
    """Represent a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """Size"""
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """Initialize atrib"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1


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
                string += (str(self.print_symbol) * (self.__width))
                if i != self.__height - 1:
                    string += "\n"

            return string



    def __repr__(self):
        """Repr for eval"""

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
            """Delete object"""
            Rectangle.number_of_instances -= 1
            print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Stat_met"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2





