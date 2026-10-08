
"""Define the Square class using Rectangle inheritance."""

from rectangle import Rectangle


class Square(Rectangle):
    """Represent a square with equal length, width, and side."""

    def __init__(self, side, name="Square"):
        """Initialize a square using equal rectangle dimensions."""
        super().__init__(side, side, name)
        self._side = self._length

    @property
    def side(self):
        """Return the square's positive side length."""
        return self._side

    @side.setter
    def side(self, value):
        """Update side, length, width, and area together."""
        self._set_side(value)

    @property
    def length(self):
        """Return the square's length, equal to its side."""
        return self._length

    @length.setter
    def length(self, value):
        """Change both dimensions to preserve a square."""
        self._set_side(value)

    @property
    def width(self):
        """Return the square's width, equal to its side."""
        return self._width

    @width.setter
    def width(self, value):
        """Change both dimensions to preserve a square."""
        self._set_side(value)

    def _set_side(self, value):
        """Validate and synchronize all square dimensions."""
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Side must be numeric.")
        if value <= 0:
            raise ValueError("Side must be greater than zero.")

        self._side = value
        self._length = value
        self._width = value
        self.calc_area()
