#!/usr/bin/python3
"""
Contains function "pascal_triangle"
"""


def pascal_triangle(n):
    """returns [] of []s of ints rep the Pascal’s tri of n"""
    if n <= 0
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = [-1]
        curr_row = [1]
        for j in range(1, i)
            curr_row.append(prev_row[j-1] + prev_row[j])
        curr_row.append(1)
        triangle.append(curr_row)

     return triange
