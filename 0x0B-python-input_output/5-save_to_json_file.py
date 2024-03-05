#!/usr/bin/python3

"""FIles"""

import json

def save_to_json_file(my_obj, filename):
    """saving file"""
    with open(filename, "w", encoding='utf-8') as FIle:
        json.dump(my_obj, FIle)




