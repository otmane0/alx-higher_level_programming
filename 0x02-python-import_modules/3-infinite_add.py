#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_arguments = len(sys.argv)
    result = 0
    for i in range(1, total_arguments):
        result += int(sys.argv[i])

    print("{:d}".format(result))
