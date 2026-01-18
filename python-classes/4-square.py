#!/usr/bin/python3
"""Defines a Square class with a private size and a property for size."""

class Square:
    """Represent a square with size validation via a property."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): size of a side (default 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """
        self.size = size  # use the setter for validation

    @property
    def size(self):
        """Retrieve the size (getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size (setter) with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
