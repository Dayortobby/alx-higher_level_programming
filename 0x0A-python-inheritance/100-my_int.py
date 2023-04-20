#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """
    A rebel int that inverts the == and != operators.
    """
    def __eq__(self, other):
        """Return the opposite of == operator."""
        return super().__ne__(other)
    
    def __ne__(self, other):
        """Return the opposite of != operator."""
        return super().__eq__(other)
