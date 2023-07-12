#!/usr/bin/python3
import math
"""
Main file for testing
"""


def minOperations(n):
    """
    :param n:
    :return: int
    """
    if n == 1:
        return 0

    primeFactors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            primeFactors.append(i)
            n //= i
    if n > 1:
        primeFactors.append(n)

    minimumNum = sum(primeFactors)
    return minimumNum
