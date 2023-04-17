#!/usr/bin/python3
"""
contains inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance
    of a class that inherited 
    (directly or indirectly) from 
    the specified class; else False
    """
    return (issubclass(obj, a_class))
