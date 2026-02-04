#!/usr/bin/python3
"""Module defining BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry with area() and integer_validator()"""

    def area(self):
        """Raise exception: area() not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
