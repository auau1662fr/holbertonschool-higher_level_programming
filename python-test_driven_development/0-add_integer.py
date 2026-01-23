#!/usr/bin/python3
"""
Module that adds two integers
"""


def add_integer(a, b=98):
    """Add two integers or floats (cast to int).

    Args:
        a: first number
        b: second number (default 98)

    Raises:
        TypeError: if a or b is not int or float

    Returns:
        int: sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
