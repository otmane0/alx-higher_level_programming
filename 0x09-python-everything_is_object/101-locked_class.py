#!/usr/bin/python3
"""
This module contains the definition of the lockedClass
"""


class LockedClass:
    """
    A class that prevents the user from dynamically creating new instance
    attributes,except if the new instance attribute is called first_name.
    """

    __slots__ = ['first_name']
