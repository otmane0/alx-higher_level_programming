#!/usr/bin/python3
"""add/don't add"""

save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

import sys

arguments = list(sys.argv[1:])

try:
    old_data = load_from('add_item.json')
except Exception:
    old_data = []

old_data.extend(arguments)
save_to(old_data, 'add_item.json')



