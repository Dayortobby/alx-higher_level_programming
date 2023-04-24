#!/usr/bin/python3
"""
Contains class_to_json function
"""


def class_to_json(obj):
    """returns dictionary description with simple data structure 
    (list, dictionary, string, integer and boolean)
    for json serialisation of an object"""
    return obj.__dict__
