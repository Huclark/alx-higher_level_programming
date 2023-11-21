#!/usr/bin/python3
"""Defines a square
"""


class Square:
    """Definition goes here
    """
    def __init__(self, size=0):
        """Initializes a Square instance

        Args:
            size (int, optional): Size of square. Defaults to 0.

        Note:
            The size parameter is a private instance attribute
        """
        self.size = size

    @property
    def size(self):
        """Gets the variable and returns it
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the variable and handles errors

        Args:
            size (int): Size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the square area of the current square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for column in range(self.__size):
                for row in range(self.__size):
                    print("{}".format("#"), end="")
                print()
