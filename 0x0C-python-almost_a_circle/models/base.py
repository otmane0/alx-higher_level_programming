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
        if list_objs is None:
            list_objs = []

        json_list = [ob.to_dictionary() for ob in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as F:
            F.write(json.dumps(json_list))
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)








