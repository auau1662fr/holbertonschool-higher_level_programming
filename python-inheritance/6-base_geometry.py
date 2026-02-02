#!/usr/bin/python3
class BaseGeometry:
    """BaseGeometry class with an unimplemented area method."""

    def area(self):
        """Raises an exception indicating the area method is not implemented."""
        raise Exception("area() is not implemented")
