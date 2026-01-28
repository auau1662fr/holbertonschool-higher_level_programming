#!/usr/bin/python3
"""Defines a Square with a private size attribute."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size):
        """Initialize the square with a private size."""
        self.__size = size
