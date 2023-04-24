#!/usr/bin/python3
"""
Script that adds all args to a py list, & then save them to a file
"""

import sys
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file

filename = "add_item.json"

"""load existing list from the file, or create an empty list"""
try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    json_list = []

"""Add the command line arguments to the list"""
for arg in sys.argv[1:]:
    json_list.append(arg)

"""Save the updated list to the file"""
save_to_json_file(json_list, filename)
