#!/usr/bin/python3
"""Demonstrating Python Classes
"""


class Base:
    """A Base class instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialilzation of a Base class instance

        Args:
            id (int, optional): id attribute. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
