#!/usr/bin/python3
"""
0-main
"""


def island_perimeter(grid):
    """
    GRID"""
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Check top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 for each shared side

    return perimeter
