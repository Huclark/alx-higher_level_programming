#!/usr/bin/python3
"""Class and JSON implementation
"""


class Student:
    """A Student class
    """
    def __init__(self, first_name, last_name, age):
        """Initialization of a Student class instance

        Args:
            first_name (str): First name of student
            last_name (str): Student's last name
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description for JSON
        serialization

        Args:
            attrs (list, optional): List of attributes. Defaults to None.

        Returns:
            dict: The dictionary description
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            if a in self.__dict__:
                new_dict[a] = self.__dict__[a]
        return new_dict
