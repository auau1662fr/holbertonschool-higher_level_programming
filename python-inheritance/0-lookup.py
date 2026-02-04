#!/usr/bin/python3
"""Module defining lookup function"""


def lookup(obj):
    """Return list of available attributes and methods of obj."""
    return dir(obj)
