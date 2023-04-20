#!/usr/bin/python3
"""
Defines a MyInt class that inherits from int and inverts the == and != operators.
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
