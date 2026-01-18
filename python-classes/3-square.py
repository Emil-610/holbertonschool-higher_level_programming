#!/usr/bin/python3
"""Defines a Square class with a private size and an area method."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): size of a side (default 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
