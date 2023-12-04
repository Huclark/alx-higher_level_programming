#!/usr/bin/python3
"""Implementing a Rectangle subclass
"""


# Get the Rectangle subclass
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A grand child class to handle squares
    """
    def __init__(self, size):
        """Initializes a Square instance

        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)

        super().__init__(size, size)

        self.__size = size

    def __str__(self):
        """Prints a string

        Returns:
            str: A string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
