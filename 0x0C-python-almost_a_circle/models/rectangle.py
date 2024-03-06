#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.Validate_attributes("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.Validate_attributes("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.Validate_attributes("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.Validate_attributes("y", value)
        self.__y = value

    def  Validate_attributes(self, name, value, eql=True):
        """Methode for validate all attrbutes"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eql and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eql and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """return area"""
        return self.__width * self.__height

    def display(self):
        """desplay"""
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height)


    def _update(self, id=None, width=None, height=None, x=None, y=None):
        """args"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args):
        """printing args/kwargs"""
        if args:
            self._update(*args)





