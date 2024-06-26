#!/usr/bin/python3
"""Task 0: Solution to the N Queens Problem"""
import sys


def is_horizontal(current, new):
    """Checks if the new item is horizontally
    aligned with any of the existing items"""

    for item in current:
        if item[0] == new[0]:
            return True

    return False


def is_vertical(current, new):
    """Checks if the new item is vertically
    aligned with any of the existing items"""

    for item in current:
        if item[1] == new[1]:
            return True

    return False


def is_diagonal(current, new):
    """Checks if the new item is diagonally
    aligned with any of the existing items"""

    for item in current:
        row_diff = item[0] - new[0]
        col_diff = item[1] - new[1]
        if row_diff < 0:
            row_diff *= -1

        if col_diff < 0:
            col_diff *= -1

        if row_diff == col_diff:
            return True

    return False


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    res = []
    """The list of solutions to the N queens problem."""
    queue = []
    """The list of possible solutions to the N queens problem."""

    for c in range(0, N):
        queue.append([[0, c]])

    while len(queue) > 0:
        cur = queue.pop(0)
        if len(cur) == N:
            res.append(cur)
            continue
        r = cur[-1][0] + 1

        for c in range(0, N):
            if (
                (not is_horizontal(cur, [r, c])) and
                (not is_vertical(cur, [r, c])) and
                (not is_diagonal(cur, [r, c]))
            ):
                queue.append(cur + [[r, c]])

    for sol in res:
        print(sol)
