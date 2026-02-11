#!/usr/bin/python3
""" Student module
"""


class Student:
    """ Student class with first_name, last_name, age """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns a dictionary representation of the Student instance """
        return self.__dict__.copy()
