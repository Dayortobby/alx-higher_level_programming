#!/usr/bin/python3
"""
checking if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """return True if object is exactly an instance of the specified class"""
    return (type(obj) == a_class)
