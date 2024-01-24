#!/usr/bin/python
for i in range(0, 100):
    if i == 99:
        print("{:d}\n".format(i),end="")
    else:
        print("{:d}".format(i), end= ", ")
