#!/usr/bin/python3
"""Define"""
import json
def load_from_json_file(filename):
    """Write"""
    with open(filename, "w", encoding="utf-8") as file:
        json.load(file, filename)

