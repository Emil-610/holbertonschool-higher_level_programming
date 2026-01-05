#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: size of the square (no type/value verification here)
        """
        self.__size = size
