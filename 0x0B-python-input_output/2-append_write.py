#!/usr/bin/python3
"""
contains function a "append_write"
"""


def append_write(filename="", text=""):
    """""returns the number of chars added"""
    with open(filename,  "a", encoding="utf-8") as f:
        return f.write(text)
