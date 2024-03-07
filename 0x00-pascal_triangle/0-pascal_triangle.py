#!/usr/bin/python3

"""Defines the pascal_triangle function"""


def pascal_triangle(n):
    """
    Creates a pascals triangle

    Args:
        n (int): height of the pascal's triangle

    Returns:
        A list of lists of integers representing the Pascal’s triangle of n.
    """
    result = []
    if n <= 0:
        return result

    result.append([1])
    if n == 1:
        return result

    result.append([1, 1])
    if n == 2:
        return result

    for _ in range(3, n + 1):
        row = [1]
        for i in range(1, len(result[-1])):
            row.append(result[-1][i - 1] + result[-1][i])
        row.append(1)
        result.append(row)

    return result
