#!/usr/bin/python3
"""
contains class BaseGeometry
"""


class BaseGeometry(object):
    """initiating the class methods"""
    def __init__(self):
        pass
    """a public instance that raises an execption when called"""
    def area(self):
        raise Exception("area() is not implemented")
