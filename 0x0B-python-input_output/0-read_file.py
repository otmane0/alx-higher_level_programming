#!/usr/bin/python3
"""file work"""

def read_file(filename=""):
    """read file"""

    with open(filename, "r", encoding='utf-8') as FILE:
        print(FILE.read(), end="")
