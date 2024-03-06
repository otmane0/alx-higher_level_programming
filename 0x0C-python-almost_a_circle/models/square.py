#!/usr/bin/python3
"""Square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init func"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id, self.__x, self.__y, self.__size)