#!/usr/bin/python3
"""Defines a square
"""


class Square:
    """Class definition goes here
    """
    def __init__(self, size):
        """Initialize a Square instance

        Args:
            size (int): size of square

        Note:
            The size parameter is a private instance with no type/value
            verification.
        """
        self.__size = size
