#!/usr/bin/python3
"""
contains class: Mylist
"""


class MyList(list):
    """ a subclass of list"""
    def __init__(self):
        """initiates the object"""
        super().__init__()
        
    def print_sorted(self):
        """prints out the sorted list"""
        print(sorted(self))
