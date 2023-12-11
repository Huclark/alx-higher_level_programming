#!/usr/bin/python3
"""Unit tests for rectangle.py
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class.
    """
    def test_default_values(self):
        """Test instantiation with default values."""
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_custom_values(self):
        """Test instantiation with custom values."""
        r = Rectangle(5, 10, 2, 3, 15)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 15)

    def test_invalid_width(self):
        """Test that invalid width raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_invalid_height(self):
        """Test that invalid height raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(5, -10)

    def test_invalid_x(self):
        """Test that invalid x raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3)

    def test_invalid_y(self):
        """Test that invalid y raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3)

    def test_invalid_width_type(self):
        """Test that invalid width type raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10)

    def test_invalid_height_type(self):
        """Test that invalid height type raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(5, "invalid")

    def test_invalid_x_type(self):
        """Test that invalid x type raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid", 3)

    def test_invalid_y_type(self):
        """Test that invalid y type raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, "invalid")

if __name__ == "__main__":
    unittest.main()
