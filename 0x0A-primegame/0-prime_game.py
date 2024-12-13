#!/usr/bin/python3
"""
This module defines functions to determine the winner
based on optimal gameplay in the prime game
"""


def is_prime(num):
    """Helper function to check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def sieve_of_eratosthenes(max_num):
    """
    Helper function to precompute prime counts using the Sieve of Eratosthenes
    """
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    return prime_count


def isWinner(x, nums):
    """
    Determine the winner of the prime game
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    prime_count = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
