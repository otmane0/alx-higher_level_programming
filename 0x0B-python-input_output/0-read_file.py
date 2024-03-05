#!/usr/bin/python3

def read_file(filename=""):
    """read file"""
    filename = "UTF8"
    with open(filename, "r") as file:
        print(file.read())
