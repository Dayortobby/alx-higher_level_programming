#!/usr/bin/python3
"""
Contains class Student
"""


class Student(object):
    """Rep a student"""
    def __init__(self, first_name, last_name, age):
        """Initialises a new student
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def class_to_json(obj):
        return obj.__dict__

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                 all(type(ele) == str for ele in attrs)):
            return{k: getattr(self, k) for k in attrs if hasattr(sef, k)}
        retutn self.__dict__
