#!/usr/bin/python3
"""FIles"""

import json
"""json works"""

def load_from_json_file(filename):
    with open(filename, "r", encoding='utf-8') as FIle:
        return json.load(filename)
