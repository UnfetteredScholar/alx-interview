#!/usr/bin/python3
"""Defines island_perimeter function"""


def map_island(r: int, c: int, grid: list) -> int:
    """Maps the perimeter of an island"""
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 0
    if grid[r][c] != 1:
        return 0

    sum = 0
    if r + 1 >= len(grid) or grid[r + 1][c] == 0:  # Top
        sum += 1
    if r - 1 < 0 or grid[r - 1][c] == 0:  # Bottom
        sum += 1
    if c + 1 >= len(grid[0]) or grid[r][c + 1] == 0:  # Right
        sum += 1
    if c - 1 < 0 or grid[r][c - 1] == 0:  # Left
        sum += 1
    grid[r][c] = 2

    return (
        sum
        + map_island(r - 1, c, grid)
        + map_island(r + 1, c, grid)
        + map_island(r, c - 1, grid)
        + map_island(r, c + 1, grid)
    )


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    # Find part of the island
    r = -1
    c = -1

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                r = row
                c = col
    if r == -1 and c == -1:
        return 0

    return map_island(r, c, grid)
