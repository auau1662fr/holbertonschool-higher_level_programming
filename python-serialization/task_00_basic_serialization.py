#!/usr/bin/python3
""" Basic Serialization Module """

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): JSON output file path
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and deserialize it to a Python dictionary.

    Args:
        filename (str): JSON input file path

    Returns:
        dict: The Python dictionary obtained from the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
