#!/usr/bin/python3

import json

class Student:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

student_1 = Student("otmane", "kasmi", 24)

json_string = json.dumps(student_1.to_json())

print(json_string)
