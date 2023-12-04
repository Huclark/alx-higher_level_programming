#!/usr/bin/python3
"""Implementing a BaseGeometry class
"""


# Get the BaseGeometry class
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A child class"""
    def __init__(self, width, height):
        """Initializes a Rectangle class instance

        Args:
            width (int): width
            height (int): height
        """
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """Area of square

        Returns:
            int: The area of the square
        """
        return self.__width * self.__height

    def __str__(self):
        """Prints to stdout

        Returns:
            str: A string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
