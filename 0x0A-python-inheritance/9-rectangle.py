#!/usr/bin/python3
""" Module for Rectangle class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Rectangle class inheriting from BaseGeometry """
    def __init__(self, width, height):
        """ Initialize Rectangle with width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return erea"""
        return self.__width * self.__height


    def __str__(self):
        """str presentation"""
        return "[Rectangle]" + str(self.__width) + "/" + str(self.__height)



