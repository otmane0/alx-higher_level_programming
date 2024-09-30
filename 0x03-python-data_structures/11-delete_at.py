#!/usr/bin/python3
"""Write a function that deletes the item at a specific position in a list.

Prototype: def delete_at(my_list=[], idx=0):
If idx is negative or out of range, nothing change (returns the same list)
You are not allowed to use pop()
You are not allowed to import any module"""

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return(my_list)

    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])

    return (new_list)

