#!/usr/bin/python3
"""
contains a subclass Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing a Square"""
    def __init__(self, size):
        """instantiation  with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2        
