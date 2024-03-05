#!/usr/bin/python3
"""Printing"""

def is_kind_of_class(obj, a_class):
    """function is_kind_of_class"""
    if isinstance(obj, a_class) or isinstance(obj, object):
        return True
    else:
        return False
