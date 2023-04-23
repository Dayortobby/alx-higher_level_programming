#!/usr/bin/python3
"""
contains save_to_json_file function
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a .txt, using a JSON rep"""
    with open(my_obj, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
