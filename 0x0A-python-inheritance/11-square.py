#!/usr/bin/python3
"""
contains a subclass Square that inherits from Rectangle
"""

Rectange = __import__(9-rectangle.py).Rectangle


class Square(Rectangle):
    """representing a Square"""
    def __init__(self, size):
        """instatiation of the Square"""
        self.integer_validator("size", size)
        sef.__size = size

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """informal string representation of the square"""
        return "[Sqaure] {:d}/{:d}".format(self.__size, self.__size)
