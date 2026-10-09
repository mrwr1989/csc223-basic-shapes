
"""Unit tests for the Rectangle class."""

import unittest

from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test rectangle construction, dimensions, and area."""

    def test_valid_rectangle(self):
        """Verify valid length and width."""
        rectangle = Rectangle(5, 4)
        self.assertEqual(rectangle.length, 5)
        self.assertEqual(rectangle.width, 4)

    def test_initial_area(self):
        """Verify area equals length times width."""
        rectangle = Rectangle(5, 4)
        self.assertAlmostEqual(rectangle.area, 20)

    def test_zero_length(self):
        """Verify zero length raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 4)

    def test_negative_width(self):
        """Verify negative width raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(5, -3)

    def test_invalid_length_type(self):
        """Verify nonnumeric length raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("five", 4)

    def test_invalid_width_type(self):
        """Verify nonnumeric width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(5, "four")

    def test_length_change(self):
        """Verify changing length recalculates area."""
        rectangle = Rectangle(5, 4)
        rectangle.length = 8
        self.assertAlmostEqual(rectangle.area, 32)

    def test_width_change(self):
        """Verify changing width recalculates area."""
        rectangle = Rectangle(5, 4)
        rectangle.width = 6
        self.assertAlmostEqual(rectangle.area, 30)

    def test_failed_assignment_preserves_values(self):
        """Verify invalid updates do not change valid values."""
        rectangle = Rectangle(5, 4)

        with self.assertRaises(ValueError):
            rectangle.length = -2

        self.assertEqual(rectangle.length, 5)
        self.assertEqual(rectangle.width, 4)
        self.assertAlmostEqual(rectangle.area, 20)

    def test_custom_name(self):
        """Verify a custom rectangle name."""
        rectangle = Rectangle(5, 4, "My Rectangle")
        self.assertEqual(rectangle.name, "My Rectangle")


if __name__ == "__main__":
    unittest.main()
