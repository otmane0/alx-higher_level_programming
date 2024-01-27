#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]

    if len(arguments) == 1:
        print("{} argument:".format(len(arguments)))
    else:
        print("{} arguments:".format(len(arguments)))

    for i, arr in enumerate(arguments):
        print("{:d}: {}".format(i + 1, arr))
