#!/usr/bin/python3
"""file work"""

def write_file(filename="", text=""):
    """read file"""


    with open(filename, "w", encoding='utf-8') as File:
        File.write(text)

    return len(text)