#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student
        """
        if attrs is None:
            return self.__dict__

        elif isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            result = {}
            for attr in attrs:
                for key in self.__dict__:
                    if key == attr:
                        result[key] = self.__dict__[key]
            return result

        return self.__dict__
