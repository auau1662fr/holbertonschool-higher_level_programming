#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with validated size."""
        # Validate size using BaseGeometry's integer_validator via Rectangle
        self.integer_validator("size", size)

        # Call Rectangle's constructor with width and height = size
        super().__init__(size, size)

        # Store size as private
        self.__size = size
