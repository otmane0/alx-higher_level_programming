#!/usr/bin/python3
"""Defines a text file-reading function."""


def write_file(filename="", text=""):
    """Write in file"""
    with open(filename, "w", encoding="utf-8") as f:
            total = f.write(text)

    return total
