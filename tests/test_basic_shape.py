
"""Unit tests for the BasicShape abstract class."""

import unittest

from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square


class TestBasicShape(unittest.TestCase):
    """Test the abstract interface and shared properties."""

    def test_cannot_instantiate_abstract_class(self):
        """Verify BasicShape cannot be created directly."""
        with self.assertRaises(TypeError):
            BasicShape("Test")

    def test_subclasses_inherit_basic_shape(self):
        """Verify all concrete shapes inherit BasicShape."""
        shapes = [
            Circle(0, 0, 3),
            Rectangle(4, 5),
            Square(6)
        ]
        for shape in shapes:
            with self.subTest(shape=shape.name):
                self.assertIsInstance(shape, BasicShape)

    def test_name_property(self):
        """Verify the name property can be updated."""
        circle = Circle(0, 0, 2)
        circle.name = "My Circle"
        self.assertEqual(circle.name, "My Circle")

    def test_invalid_name_type(self):
        """Verify nonstring names raise TypeError."""
        with self.assertRaises(TypeError):
            Circle(0, 0, 2, 123)

    def test_empty_name(self):
        """Verify empty names raise ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(2, 3, "   ")

    def test_area_is_read_only(self):
        """Verify client code cannot directly change area."""
        square = Square(4)
        with self.assertRaises(AttributeError):
            square.area = 100


if __name__ == "__main__":
    unittest.main()
