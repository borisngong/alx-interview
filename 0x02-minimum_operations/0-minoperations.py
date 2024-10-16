#!/usr/bin/env python3
"""
A module to find the minimum number of operations required to get exactly
n 'H' characters using the "Copy All" and "Paste" operations
"""


def minOperations(n):
    """
    A function that takes an integer n as input and returns the minimum
    number of operations required to get exactly n 'H' characters
    """
    if n < 2:
        return 0

    numberOperation = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            numberOperation += factor
            n //= factor
        factor += 1

    return numberOperation
