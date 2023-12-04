#!/usr/bin/python3
"""Implementing a Rectangle class
"""


# Get the Rectangle class
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
