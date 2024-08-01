#!/usr/bin/python3
"""0-island_perimeter.py"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island represented by a grid.

    Args:
        grid (list): A 2D list representing the
        island, where 1 represents land and 0
        represents water.

    Returns:
        int: The perimeter of the island.

    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
