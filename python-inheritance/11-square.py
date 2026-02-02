#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle with custom __str__."""

    def __init__(self, size):
        """Initialize a Square with validated size."""
        # Validate size
        self.integer_validator("size", size)

        # Initialize as a Rectangle with width = height = size
        super().__init__(size, size)

        # Store size as private
        self.__size = size

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
