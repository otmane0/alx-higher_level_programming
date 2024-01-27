#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]


    print("{} argument:".format(len(arguments)))
    i = 0
    for i, arr in enumerate(arguments):
        print("{:d}: {}".format(i + 1, arr))
