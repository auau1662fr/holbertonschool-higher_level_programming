#!/usr/bin/python3
"""Module that defines a MyList class with a sorted print method"""


class MyList(list):
    """Custom list class"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
