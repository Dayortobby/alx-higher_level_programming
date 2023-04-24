#!/usr/bin/python3
"""
contains load_from_json_file function
"""

import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, "x", encoding="utf-8") as f:
        json.load(f)
