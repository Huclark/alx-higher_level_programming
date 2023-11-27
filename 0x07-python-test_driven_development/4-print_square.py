#!/usr/bin/python3
"""Prints a square using #
"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size (int): The size of the square
    """
    if (not isinstance(size, int) or isinstance(size, bool) or
            isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for column in range(size):
        for row in range(size):
            print("#", end="")
        print()
