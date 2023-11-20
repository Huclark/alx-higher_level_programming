#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an integer followed by a new line

    Args:
        value: Integer to print

    Return: True if value is an integer
    Otherwise, False
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
        