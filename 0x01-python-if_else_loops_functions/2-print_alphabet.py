#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i == 101 or i == 133:
        print("")
    else:
        print("{:c}".format(i), end="")
