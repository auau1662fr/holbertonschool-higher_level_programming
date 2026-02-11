#!/usr/bin/python3
"""
Function that returns the dictionary description
with simple data structure (for JSON serialization) of an object.
"""


def class_to_json(obj):
    """
    Returns a dictionary with all attributes of obj
    Args:
        obj: instance of a class
    Returns:
        dict: dictionary with all attributes
    """
    return obj.__dict__
