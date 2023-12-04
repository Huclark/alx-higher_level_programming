#!/usr/bin/python3
"""Demonstrates the use of classes"""


class BaseGeometry:
    """A BaseGeometry class
    """
    def area(self):
        """Raises an exception

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
