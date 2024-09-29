#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    for n in range(i - 1, -1, -1):
        print(f"{my_list[n]}", end="\n")