#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    """

    triangle = []
    if n <= 0:
        return []

    firstrow = [1]
    triangle.append(firstrow)
    if n == 1:
        return triangle

    for i in range(1, n):
        prevRow = triangle[i - 1]
        next_row = []
        next_row.append(1)
        for j in range(i - 1):
            next_row.append(prevRow[j] + prevRow[j + 1])
        next_row.append(1)
        triangle.append(next_row)

    return triangle
