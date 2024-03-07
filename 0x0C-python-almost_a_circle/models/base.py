#!/usr/bin/python3
"""Project"""

import json

class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """using json"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]

        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as FILE:
            FILE.write(cls.to_json_string(list_objs))






