#!/usr/bin/python3
"""FIles"""

import json

def load_from_json_file(filename):
    """an object from json"""
    with open(filename, "r", encoding='utf-8') as FIle:
        return json.load(FIle)
