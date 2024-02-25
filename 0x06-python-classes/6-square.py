#!/usr/bin/python3
class Square:
    """
    Access and update private attribute
    """
    def __init__(self, size=0, position=(0, 0)) :
        self.size = size
        self.position = position

    def area(self):
        """
        Access and update private attribute
        """
        return self.size * self.size

    @property
    def size(self):
        """
        Access and update private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Access and update private attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Access and update private attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Access and update private attribute
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(v, int) and v >= 0 for v in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
