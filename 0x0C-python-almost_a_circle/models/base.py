#!/usr/bin/python3
"""Project"""
class Base:
    """blass Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """For all"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id += Base.__nb_objects