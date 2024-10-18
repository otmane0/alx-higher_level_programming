#!/usr/bin/python3

"""We do return self7__dict__, to set key, value like a dictionry"""

class Student:
    """Class"""
    def __init__(self, first_name, last_name, age):
        """Init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To dict"""
        if attrs == None:
            return self.__dict__
        else:
            filtered_dict = []
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)

            return filtered_dict.__dict__