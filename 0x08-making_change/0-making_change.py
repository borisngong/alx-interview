#!/usr/bin/python3
"""Module to determine the fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """
    Responsible for determining the fewest number of coins needed
    to meet a given total
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for greedy-like optimization
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            count += total // coin  # Add the number of coins
            total %= coin  # Reduce the remaining total

    return count if total == 0 else -1
