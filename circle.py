
"""Define the Circle class for the basic-shapes hierarchy."""

from math import pi
from basic_shape import BasicShape


class Circle(BasicShape):
    """Represent a circle with a center and positive radius."""

    def __init__(self, x_center, y_center, radius, name="Circle"):
        """Initialize the circle's center, radius, and name."""
        super().__init__(name)
        self._x_center = 0
        self._y_center = 0
        self._radius = None

        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    @property
    def x_center(self):
        """Return the numeric x-coordinate of the center."""
        return self._x_center

    @x_center.setter
    def x_center(self, value):
        """Set the x-coordinate; it must be numeric."""
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("X-coordinate must be numeric.")
        self._x_center = value

    @property
    def y_center(self):
        """Return the numeric y-coordinate of the center."""
        return self._y_center

    @y_center.setter
    def y_center(self, value):
        """Set the y-coordinate; it must be numeric."""
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Y-coordinate must be numeric.")
        self._y_center = value

    @property
    def radius(self):
        """Return the positive radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Validate radius and automatically recalculate area."""
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Radius must be numeric.")
        if value <= 0:
            raise ValueError("Radius must be greater than zero.")
        self._radius = value
        self.calc_area()

    def calc_area(self):
        """Calculate and store the circle's area."""
        self._area = pi * self._radius ** 2
        return self._area
