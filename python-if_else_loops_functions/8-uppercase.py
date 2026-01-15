#!/usr/bin/python3

def uppercase(str):
    """
    Prints a string in uppercase followed by a new line.

    Args:
        str (str): the string to convert to uppercase
    """
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()
