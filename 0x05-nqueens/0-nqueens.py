#!/usr/bin/python3
"""Task 0"""
from sys import argv


def is_horizontal(current: list, new: list) -> bool:
    """Checks if the new item is horizontally
    aligned with any of the existing items"""

    for item in current:
        if item[0] == new[0]:
            return True

    return False


def is_vertical(current: list, new: list) -> bool:
    """Checks if the new item is vertically
    aligned with any of the existing items"""

    for item in current:
        if item[1] == new[1]:
            return True

    return False


def is_diagonal(current: list, new: list) -> bool:
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

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(argv[1])
    except Exception:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    res = []
    queue = []

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
                (not is_horizontal(cur, [r, c]))
                and (not is_vertical(cur, [r, c]))
                and (not is_diagonal(cur, [r, c]))
            ):
                queue.append(cur + [[r, c]])

    for sol in res:
        print(sol)
