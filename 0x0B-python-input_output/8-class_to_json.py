#!/usr/bin/python3
"""
Contains class_to_json function
"""


def class_to_json(obj):
    """returns dict descript for json object"""
    return obj.__dict__
