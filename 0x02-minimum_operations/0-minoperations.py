#!/usr/bin/python3
"""
Defines the function minOperations
"""


def isPrime(num: int) -> bool:
    """Checks in a number is prime"""
    i = 2
    mid = num / 2
    while i < mid:
        if num % i == 0:
            return False
        i += 1
    return True


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

    if type(n) is not int:
        return 0

    while count < n:
        if (n % count == 0) and isPrime(count):
            clipboard = count
            operations += 1
        count += clipboard
        operations += 1
    return operations
