#!/usr/bin/python3

"""Prints the number of and the list of its arguments"""

from sys import argv

if __name__ == "__main__":

    argc = len(argv)

    if argc == 2:
        print("{} argument:".format(argc - 1))
    else:
        print("{} arguments".format(argc - 1, "." if argc == 1 else ":"))

    if argc > 1:
        for i in range(1, argc):
            print("{}: {}".format(i, argv[i]))
