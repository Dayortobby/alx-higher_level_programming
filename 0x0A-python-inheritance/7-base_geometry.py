#!/usr/bin/python3
"""
contains a class BaseGeometry
"""


class BaseGeometry:
    """intiating the class methods"""
    def __init__(self):
        pass
    """raises an Exception"""
    def area(self):
        raise Exception("area() is not implemented")
    """validates value"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
