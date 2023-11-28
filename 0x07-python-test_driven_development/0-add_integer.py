#!/usr/bin/python3
"""Returns a + b
"""


def add_integer(a, b=98):
    """This function adds two integers

    Args:
        a (int): 1st integer input
        b (int, optional): 2nd integer input. Defaults to 98.

    Returns:
        Addition of a and b

    Note:
        Floats are typecast into integers
    """
    # Check if a is an integer or float
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")

    # Check if b is an integer or float
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    # Typecast to int when returning addition
    return int(a) + int(b)
