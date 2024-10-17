#!/usr/bin/python3
"""Define"""

import json

def load_from_json_file(filename):
    """Write"""

    with open(filename, "w") as file:
        return json.load(file)
