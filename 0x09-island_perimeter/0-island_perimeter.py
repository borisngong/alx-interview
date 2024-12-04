#!/usr/bin/python3
"""
module to calculate the perimeter of an island in a given grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 sides for the land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:  # Check top
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
