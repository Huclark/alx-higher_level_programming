#!/usr/bin/python3
"""A Square class that inherits from a Rectangle
class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance

        Args:
            size (int): Size of square
            x (int, optional): x co-ordinate. Defaults to 0.
            y (int, optional): y co-ordinate. Defaults to 0.
            id (int, optional): Unique identifier for the class.
                                Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size of square

        Returns:
            int: value of width
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value for size

        Args:
            value (int): size of square

        Raises:
            TypeError: integer type
            ValueError: value should be greater than 0
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for idx in range(len(args)):
                setattr(self, attributes[idx], args[idx])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """returns a string

        Returns:
            str: a string
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Represents the square in a dictionary

        Returns:
            dict: The dictionary representation of a square
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
