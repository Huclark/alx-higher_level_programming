#!/usr/bin/python3
"""A Rectangle class that inherits from a Base
class
"""


from models.base import Base


class Rectangle(Base):
    """A Rectangle class which inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of a Rectangle instance

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int, optional): x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): Unique identifier for the class.
                                Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width

        Returns:
            int: value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width

        Args:
            value (int): value of width

        Raises:
            TypeError: integer type
            ValueError: value should be greater than 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height

        Returns:
            int: value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height

        Args:
            value (int): value of height

        Raises:
            TypeError: integer type
            ValueError: value should be greater than 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x

        Returns:
            int: value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x

        Args:
            value (int): value of x

        Raises:
            TypeError: integer type
            ValueError: value should be greater than 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y

        Returns:
            int: value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y

        Args:
            value (int): value of y

        Raises:
            TypeError: integer type
            ValueError: value should be greater than 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Determines the area value of the Rectangle instance

        Returns:
            int: The area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the
        character, "#".
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a string

        Returns:
            str: returns a string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for idx in range(len(args)):
                setattr(self, attributes[idx], args[idx])
        elif kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Represents the rectangle in a dictionary

        Returns:
            dict: The dictionary representation of a rectangle
        """
        return {'x': self.x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
