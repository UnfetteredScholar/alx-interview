#!/usr/bin/python3
"""Defines makeChange function"""


def makeChange(coins, total):
    """
    Determines the fewest number of
    coins needed to meet a given amount total
    """
    if total <= 0:
        return -1

    coins = sorted(coins, key=lambda x: -x)
    solutions = []  # (count, remainder)
    # [1, 2, 25], 37)
    for coin in coins:
        solutions.append([0, total])

        for sol in solutions:
            diff = sol[1] % coin
            sol[0] += (sol[1] - diff) / coin
            sol[1] = diff

            if sol[1] == 0:
                return int(sol[0])

    return -1
