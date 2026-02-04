#!/usr/bin/python3
"""Module defining Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with __str__ override."""

    def __init__(self, size):
        """Initialize square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return string representation."""
        return "[Square] {}/{}".format(self.__size, self.__size)
