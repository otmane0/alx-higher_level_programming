#!/usr/bin/python3
"""Define"""
import json
def save_to_json_file(my_obj, filename):
    """Write"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))

