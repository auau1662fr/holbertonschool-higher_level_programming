#!/usr/bin/python3
"""Task 01 - Pickling Custom Classes"""

import pickle


class CustomObject:
    """A custom object that can be serialized with pickle."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        """Serialize the current instance to a file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            # Return None on error (fail silently)
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file."""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            # Return None if file does not exist or is corrupted
            return None
