#!/usr/bin/python3
def append_write(filename="", text=""):
    """Appends a string to a text file (UTF-8) and returns the number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
