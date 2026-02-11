#!/usr/bin/python3
"""Module to append a string to a file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
