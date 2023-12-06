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

    def to_json(self):
        """Returns the dictionary description for JSON
        serialization

        Returns:
            dict: The dictionary description
        """
        return self.__dict__
