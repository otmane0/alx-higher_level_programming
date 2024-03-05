#!/usr/bin/python3
"""Files"""

import json

def to_json_string(my_obj):
    """json"""

    dico = json.dump(my_obj)
    return dico
