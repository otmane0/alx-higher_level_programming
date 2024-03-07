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
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """get it"""
        return self.width
    @size.setter
    def size(self, value):
        self.width = value


    def _update(self, id=None, size=None, x=None, y=None):
        """for up func"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y


    def update(self, *args, **kwargs):
        """up func"""

        if args:
            self._update(*args)
        if kwargs:
            self._update(**kwargs)

    def to_dictionary(self):
        """To dict"""

        return { "id": self.id, "width": self.__width,"height": self.__height, "x": self.__x,"y": self.__y}



