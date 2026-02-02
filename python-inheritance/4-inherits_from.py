#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class, but not a_class itself."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
