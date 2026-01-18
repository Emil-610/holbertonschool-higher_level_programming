#!/usr/bin/python3
"""Defines a Square class with size and position."""


class Square:
    """Represent a square with size and position validation."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): side length (default 0)
            position (tuple): (horizontal_offset, vertical_offset) (default (0, 0))
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position (getter)."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position (setter) with validation.

        position must be a tuple of 2 positive integers (>= 0).
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character.

        Prints vertical offset (position[1]) as blank lines first.
        Each printed line is prefixed by position[0] spaces.
        If size is 0, prints a single empty line.
        """
        if self.__size == 0:
            print()
            return

        # vertical offset
        if self.__position[1] > 0:
            print("\n" * self.__position[1], end="")

        # each line: horizontal offset spaces + size '#' characters
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
