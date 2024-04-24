#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n: The number of rows in the triangle.

    Returns:
        A list of lists representing the Pascal's triangle.
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
