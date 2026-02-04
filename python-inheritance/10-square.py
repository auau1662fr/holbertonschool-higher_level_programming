#!/usr/bin/python3
"""Module defining Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size):
        """Initialize square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
