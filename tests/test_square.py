
"""Unit tests for the Square class."""

import unittest

from square import Square
from rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test square inheritance, validation, and dimensions."""

    def test_valid_square(self):
        """Verify a square is constructed correctly."""
        square = Square(5)
        self.assertEqual(square.side, 5)
        self.assertEqual(square.length, 5)
        self.assertEqual(square.width, 5)

    def test_inherits_rectangle(self):
        """Verify Square inherits from Rectangle."""
        square = Square(4)
        self.assertIsInstance(square, Rectangle)

    def test_initial_area(self):
        """Verify square area is side squared."""
        square = Square(4)
        self.assertAlmostEqual(square.area, 16)

    def test_side_change(self):
        """Verify changing side updates all dimensions."""
        square = Square(4)
        square.side = 7
        self.assertEqual(square.side, 7)
        self.assertEqual(square.length, 7)
        self.assertEqual(square.width, 7)
        self.assertAlmostEqual(square.area, 49)

    def test_length_change(self):
        """Verify changing length preserves equal sides."""
        square = Square(4)
        square.length = 6
        self.assertEqual(square.side, 6)
        self.assertEqual(square.length, 6)
        self.assertEqual(square.width, 6)
        self.assertAlmostEqual(square.area, 36)

    def test_width_change(self):
        """Verify changing width preserves equal sides."""
        square = Square(4)
        square.width = 8
        self.assertEqual(square.side, 8)
        self.assertEqual(square.length, 8)
        self.assertEqual(square.width, 8)
        self.assertAlmostEqual(square.area, 64)

    def test_zero_side(self):
        """Verify zero side raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_negative_side(self):
        """Verify negative side raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-3)

    def test_invalid_side_type(self):
        """Verify nonnumeric side raises TypeError."""
        with self.assertRaises(TypeError):
            Square("five")

    def test_failed_assignment(self):
        """Verify an invalid change preserves the square."""
        square = Square(5)
        with self.assertRaises(ValueError):
            square.side = -2
        self.assertEqual(square.side, 5)
        self.assertEqual(square.length, 5)
        self.assertEqual(square.width, 5)
        self.assertAlmostEqual(square.area, 25)

    def test_custom_name(self):
        """Verify a custom square name."""
        square = Square(3, "My Square")
        self.assertEqual(square.name, "My Square")


if __name__ == "__main__":
    unittest.main()
