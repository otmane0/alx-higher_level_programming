#!/usr/bin/python3
"""Files"""


def append_write(filename="", text=""):
    """append"""

    with open(filename, "a", encoding='utf-8') as FIle:
        FIle.write(text)

    return len(text)