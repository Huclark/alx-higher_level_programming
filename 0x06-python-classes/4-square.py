#!/usr/bin/python3
"""Defines a square
"""


class Square:
    """Defintion goes here
    """
    def __init__(self, size=0):
        """Initializes a Square instance

        Args:
            self (int, optional): The size of the square. Defaults to 0.

        Note:
            The size parameter a private instance attribute.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size value

        Args:
            value (int): Size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the square area

        Returns:
            int: The current square area
        """
        return self.__size ** 2
