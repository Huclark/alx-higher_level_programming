#!/usr/bin/python3
"""Defines a Square class
"""


class Square:
    """Definiton goes here
    """
    def __init__(self, size=0):
        """Initialize a Square instance

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Note:
            The size parameter is a private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
