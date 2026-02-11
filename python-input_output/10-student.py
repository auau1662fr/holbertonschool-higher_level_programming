#!/usr/bin/python3
""" Student class with JSON representation and filtered attributes """


class Student:
    """Defines a student with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.
        If attrs is a list of strings, only include those attributes.
        The order of keys follows: age, last_name, first_name
        """
        # dictionnaire complet dans l'ordre attendu
        all_attrs = {
            'age': self.age,
            'last_name': self.last_name,
            'first_name': self.first_name
        }

        if attrs is None:
            return all_attrs
        # filtrage des attributs présents dans attrs
        return {k: all_attrs[k] for k in attrs if k in all_attrs}
