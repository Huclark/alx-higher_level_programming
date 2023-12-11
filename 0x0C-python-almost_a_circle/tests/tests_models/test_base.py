#!/usr/bin/python3
"""Unit tests for base.py
"""

import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """Testing instantiation of a Base class
    """
    def test_id_incrementation(self):
        """Test if id is incremented correctly and is
        correctly set to the right value when a custom
        id is provided
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        b4 = Base()
        b5 = Base(6)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 10)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 6)

    def test_id_independence(self):
        """Test if id is independent among instances
        """
        b1 = Base()
        b2 = Base()

        b1.id = 25

        self.assertNotEqual(b1.id, 1)
        self.assertEqual(b1.id, 25)
        self.assertNotEqual(b2.id, 25)

    def test_id_type(self):
        """Test if the id is an int
        """
        b1 = Base()

        self.assertIsInstance(b1.id, int)

    def test_private_attribute(self):
        """Test accessing the private attribute __nb_object
        """
        with self.assertRaises(AttributeError):
            print(Base(3).__nb_objects)

    def test_two_args(self):
        """Test instantiation with two arguments
        """
        with self.assertRaises(TypeError):
            Base(2, 4)

if __name__ == "__main__":
    unittest.main()
