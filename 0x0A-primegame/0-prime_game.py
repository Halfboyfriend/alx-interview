#!/usr/bin/python3
"""
0. Prime Game
"""


def isWinner(x, nums):
    """
    params"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def can_win(n):
        """
        If the number of prime numbers is even,
        Ben wins; otherwise, Maria wins
        Count the number of prime numbers in the range [2, n]
        """
        if n <= 1:
            return False
        if n <= 3:
            return True

        primes = [1] * (n + 1)
        primes[0] = primes[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = 0

        prime_count = sum(primes)
        return prime_count % 2 == 0

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if can_win(n):
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
