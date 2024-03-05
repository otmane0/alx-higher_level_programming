#!/usr/bin/python3
"""Printing"""

def inherits_from(obj, a_class):
    """true of a class"""
    return isinstance(obj, a_class) and type(obj) != a_class:
