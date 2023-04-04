#!/usr/bin/python3

def add_integer(a, b=98):
    if type(a) not in (int or float):
        raise TypeError("a must be an integer")
    if type(b) not in (int or float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
