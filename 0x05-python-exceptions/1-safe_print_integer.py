#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer with "{:d}".format()
    followed by a new line

    Args:
        value: Any data type

    Return: True if value value is an integer
    Otherwise, returns False
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
