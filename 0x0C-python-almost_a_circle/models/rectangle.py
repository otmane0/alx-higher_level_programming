#!/usr/bin/python3
"""Rectangle"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init func"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y



    @property
    def width(self):
       """width"""
       return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        self.__width = value

    @property
    def height(self):
       """height"""
       return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        self.__height = value


    @property
    def x(self):
       """x"""
       return self.__x

    @x.setter
    def x(self, value):
        """"setter"""
        self.__x = value

    @property
    def y(self):
       """y"""
       return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        self.__y = value

