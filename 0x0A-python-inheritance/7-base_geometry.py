#!/usr/bin/python3
"""A program that demonstrates classes"""


class BaseGeometry:
    """A BaseGeometry class
    """
    def area(self):
        """Raises an exception

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates "value"

        Args:
            name (str): A string
            value (int): value to validate

        Raises:
            TypeError: Checks if value is an int
            ValueError: Checks if value is greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
