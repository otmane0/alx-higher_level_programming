#!/usr/bin/python3
"""Module from a module"""
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return (dir(obj))