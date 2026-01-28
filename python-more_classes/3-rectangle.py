#!/usr/bin/python3
"""Rectangle class with string representation."""


class Rectangle(Rectangle):
    """Rectangle prints with # character."""

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
