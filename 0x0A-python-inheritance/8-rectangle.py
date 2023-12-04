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

        self.integer_validator("width", width)
        self.integer_validator("height", height)
