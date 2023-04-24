#!/usr/bin/python3
"""
contains class_to_json function
"""


def class_to_json(obj):
    """returns dictionary description with simple data structure 
    (list, dictionary, string, integer and boolean)
    for json serialisation of an object"""
    returns obj.__dict__
