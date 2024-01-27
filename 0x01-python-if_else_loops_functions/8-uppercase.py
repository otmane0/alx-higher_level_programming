#!/usr/bin/python3

def uppercase(str):
    for char in str:
        upper = ord(char)
        if 97 <= upper <= 122:
            upper -= 32
        print("{:c}".format(upper), end="")
    print()
