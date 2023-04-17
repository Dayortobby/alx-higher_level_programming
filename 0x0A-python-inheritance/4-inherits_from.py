#!/usr/bin/python3
"""
contains inherits_from function
"""


def inherits_from(obj, a_class):
    """Returns True if the object is a subclass of a_class; else False"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
