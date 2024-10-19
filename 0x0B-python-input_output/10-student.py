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
    """Get a dictionary representation of the Student.

    If attrs is a list of strings, represents only those attributes
    included in the list.

    Args:
        attrs (list): (Optional) The attributes to represent.
    """

    # If no attrs is provided, return all attributes
    if attrs == None:
        return self.__dict__

    # If attrs is a list of strings, filter for those attributes
    elif type(attrs) == list and all(type(ele) == str for ele in attrs):
        result = {}

        # Loop over each requested attribute in attrs
        for k in attrs:

            # Now check if the attribute exists in the instance's __dict__
            for key in self.__dict__:
                if key == k:
                    # Add it to the result dictionary with its value
                    result[key] = self.__dict__[key]
                    break

        # Return the filtered result
        return result

    # If attrs isn't a valid list of strings, return all attributes
    return self.__dict__
