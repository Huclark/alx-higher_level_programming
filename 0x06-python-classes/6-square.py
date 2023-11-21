#!/usr/bin/python3
"""Defines the class Square"""


class Square:
    """Definiton goes here
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square

        Args:
            size (int, optional): Size of square. Defaults to 0.
            position (tuple, optional): A tuple of 2 positive integers.
            Defaults to (0, 0).

        Note:
            The size and p = sizosition parameters are private instance
            attributes
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square

        Args:
            size (int): Size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Gets the postion

        Args:
            value (tuple): Tuple of 2 postive integers

        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
