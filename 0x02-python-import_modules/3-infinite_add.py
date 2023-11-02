#!/usr/bin/python3

"""Prints the result of the addition of all arguments"""

if __name__ == "__main__":
    from sys import argv

    result = 0

    if len(argv) == 1:
        print("{}".format(int(result)))

    else:
        for i in range(1, len(argv)):
            number = int(argv[i])
            result += number

        print("{}".format(int(result)))
