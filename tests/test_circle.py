
"""Unit tests for the Circle class."""

import unittest
from math import pi
from circle import Circle


class TestCircle(unittest.TestCase):
    """Test circle construction, validation, and area."""

    def test_valid_circle(self):
        """Verify valid coordinates and radius."""
        circle = Circle(-2, 3, 4)
        self.assertEqual(circle.x_center, -2)
        self.assertEqual(circle.y_center, 3)
        self.assertEqual(circle.radius, 4)

    def test_initial_area(self):
        """Verify the circle's initial area."""
        circle = Circle(0, 0, 3)
        self.assertAlmostEqual(circle.area, pi * 9)

    def test_zero_radius(self):
        """Verify zero radius raises ValueError."""
        with self.assertRaises(ValueError):
            Circle(0, 0, 0)

    def test_negative_radius(self):
        """Verify negative radius raises ValueError."""
        with self.assertRaises(ValueError):
            Circle(0, 0, -5)

    def test_invalid_radius_type(self):
        """Verify nonnumeric radius raises TypeError."""
        with self.assertRaises(TypeError):
            Circle(0, 0, "five")

    def test_radius_change(self):
        """Verify changing radius updates area."""
        circle = Circle(0, 0, 2)
        circle.radius = 5
        self.assertAlmostEqual(circle.area, pi * 25)

    def test_coordinate_change(self):
        """Verify moving the center does not change area."""
        circle = Circle(0, 0, 4)
        original_area = circle.area
        circle.x_center = -10
        circle.y_center = 12
        self.assertAlmostEqual(circle.area, original_area)

    def test_invalid_coordinate(self):
        """Verify nonnumeric coordinates are rejected."""
        with self.assertRaises(TypeError):
            Circle("left", 0, 3)

    def test_default_and_custom_names(self):
        """Verify default and custom circle names."""
        default_circle = Circle(0, 0, 2)
        custom_circle = Circle(0, 0, 2, "Large Circle")
        self.assertEqual(default_circle.name, "Circle")
        self.assertEqual(custom_circle.name, "Large Circle")


if __name__ == "__main__":
    unittest.main()
