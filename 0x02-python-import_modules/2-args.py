#!/usr/bin/python3

"""Prints the number of and the list of its arguments"""

if __name__ == "__main__":

    import sys

    argc = len(sys.argv)

    if argc == 1:
        print("{} arguments.".formmat(argc - 1))

    elif argc == 2:
        print("{} argument:".format(argc - 1))

    else:
        print("{} arguments:".format(argc - 1))

    if argc > 1:
        for i in range(1, argc):
            print("{}: {}". format(i, sys.argv[i]))
