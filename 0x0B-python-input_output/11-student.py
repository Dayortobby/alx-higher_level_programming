#!/usr/bin/python3
"""
contains Student Class
"""


class Student:
    """Represent a Student"""
    def __init__(self, first_name, last_name, age):
    """Initialise a new student"""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self, attrs=None):
    """Get a dictionary representation of the student"""
    if (type(attrs)) == list and
            all(type(ele)) == str for ele in attrs)):
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
    return self.__dict__

    def reload_from_json(self, json):
    """replaces all attributes of the Student"""
    for key in json:
        try:
            setattr(selt, key, json[key])
        except fileNotFounderror:
            pass
