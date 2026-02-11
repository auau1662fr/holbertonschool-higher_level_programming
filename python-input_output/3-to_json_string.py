#!/usr/bin/python3
"""Module to convert object to JSON string."""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object."""
    return json.dumps(my_obj)
