#!/usr/bin/python3
if __name__ == "__main__":

    """Prints the number of and the list of its arguments"""
    import sys

    argument_count = len(sys.argv)

    if argument_count == 1:
        print("{} arguments.".formmat(argument_count - 1))

    elif argument_count == 2:
        print("{} argument:".format(argument_count - 1))

    else:
        print("{} arguments:".format(argument_count - 1))

    if argument_count > 1:
        for i in range(1, argument_count):
            print("{}: {}". format(i, sys.argv[i]))
