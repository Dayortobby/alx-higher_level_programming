#!/usr/bin/python3
"""
Contains class Student
"""


class Student(object):
    """Rep a student"""
    def __init__(self, first_name, last_name, age):
        """Initialises a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def class_to_json(obj):
        return obj.__dict__

    def to_json(self, attrs=None):
        """Get a dict rep of the Student."""
        if (type(attrs) == list and
                 all(type(ele) == str for ele in attrs)):
            return{k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
