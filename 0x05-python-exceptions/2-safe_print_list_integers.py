#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    try:
        for j in range(x):
            if type(my_list[j]) == int:
                print("{:d}".format(my_list[j]), end="")
                counter += 1
        print()
        return counter
    except IndexError:
        print()
        return counter
