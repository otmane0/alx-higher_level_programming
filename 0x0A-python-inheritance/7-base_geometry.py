#!/usr/bin/python3
""" module of BaseGeometry class"""

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """self for printing"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer"""
        if type (value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))