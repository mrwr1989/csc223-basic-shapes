
"""Define the abstract base class for geometric shapes."""

from abc import ABC, abstractmethod


class BasicShape(ABC):
    """Represent a geometric shape with a name and area."""

    def __init__(self, name):
        """Initialize the shape's name and starting area."""
        self._name = None
        self._area = 0.0
        self.name = name

    @property
    def name(self):
        """Return the shape's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set a nonempty name, rejecting invalid values."""
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def area(self):
        """Return the calculated area (read-only)."""
        return self._area

    @abstractmethod
    def calc_area(self):
        """Calculate and store the shape's area."""
        pass
