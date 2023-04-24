#!/usr/bin/python3
"""
Contains class Student
"""


class Student(object):
    def __init__(self, first_name, last_name, age):
        self.firstname = first name
        self.last_name = lastname
        self.age = age

    def class_to_json(obj):
        return obj.__dict__

    def to_json(self):
        return self.__dict__
