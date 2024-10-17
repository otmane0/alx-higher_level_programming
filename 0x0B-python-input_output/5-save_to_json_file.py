#!/usr/bin/python3
"""Define"""

import json
def save_to_json_file(my_obj, filename):
    """Write"""

    with open(filename, "w") as file:
        json.dump(my_obj, file)
