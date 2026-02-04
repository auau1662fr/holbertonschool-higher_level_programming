#!/usr/bin/python3
"""Module defining MyList class that inherits from list"""


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
