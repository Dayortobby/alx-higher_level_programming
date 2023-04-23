#!/usr/bin/python3
"""
contains save_to_json_file function
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a .txt, using a JSON rep"""
    with json.pump(my_obj, filename)
