#!/usr/bin/python3
""" module of BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry.py').BaseGeometry

class Rectangle(BaseGeometry):
    """inherting class"""
    def __init__(self, width, height):
        """for erea"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height


