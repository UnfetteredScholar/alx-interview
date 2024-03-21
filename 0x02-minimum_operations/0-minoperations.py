#!/usr/bin/python3
"""
Defines the function minOperations
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    Operations: CopyAll and Paste

    Args:
        n: target number of characters

    Returns:
        The number of operations
    """
    count = 1
    clipboard = 0
    operations = 0

    if not isinstance(n, int):
        return 0

    while count < n:
        if (n - count) % count == 0:
            clipboard = count
            operations += 1
        count += clipboard
        operations += 1
    return operations
