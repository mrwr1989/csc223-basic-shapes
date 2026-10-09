
"""Unit tests for runtime polymorphism."""

import unittest
from math import pi

from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square


class TestPolymorphism(unittest.TestCase):
    """Verify shapes work through the BasicShape interface."""

    def setUp(self):
        """Create a collection of different shape objects."""
        self.shapes = [
            Circle(0, 0, 2),
            Circle(1, 1, 3),
            Rectangle(4, 5),
            Rectangle(6, 7),
            Square(4)
        ]

    def test_all_are_basic_shapes(self):
        """Verify every shape inherits BasicShape."""
        for shape in self.shapes:
            with self.subTest(shape=shape.name):
                self.assertIsInstance(shape, BasicShape)

    def test_common_properties(self):
        """Verify every shape has a name and area."""
        for shape in self.shapes:
            with self.subTest(shape=shape.name):
                self.assertIsInstance(shape.name, str)
                self.assertGreater(shape.area, 0)

    def test_correct_areas(self):
        """Verify each shape calculates the correct area."""
        expected = [4 * pi, 9 * pi, 20, 42, 16]

        for shape, area in zip(self.shapes, expected):
            with self.subTest(shape=shape.name):
                self.assertAlmostEqual(shape.area, area)

    def test_polymorphic_processing(self):
        """Verify mixed shapes can be processed in one loop."""
        results = []

        for shape in self.shapes:
            results.append((shape.name, shape.area))

        self.assertEqual(len(results), 5)
        self.assertEqual(results[0][0], "Circle")
        self.assertEqual(results[-1][0], "Square")


if __name__ == "__main__":
    unittest.main()
