#!/usr/bin/python3
"""Defines the isWinner function"""


def isPrime(num):
    """Determines if a number is prime"""
    if num <= 1:
        return False

    mid = int(num / 2)

    for n in range(2, mid + 1):
        if num % n == 0:
            return False

    return True


def isWinner(x, nums):
    """
    Determines the winner of x prime games
    for a set of x n's
    """
    maria = 0
    ben = 0

    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = []

    for i in range(1, max_num + 1):
        primes.append(isPrime(i))

    for n in nums:
        primes_count = 0
        for i in primes[0:n]:
            if i:
                primes_count += 1

        if primes_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
