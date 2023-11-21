#!/usr/bin/python3
"""Defines a square
"""


class Square:
    """Definition goes here
    """
    def __init__(self, size=0):
        """Initializes a square instance

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        Note:
            The size parameter is a private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area

        Returns:
            int: Current square area
        """
        return self.__size ** 2
