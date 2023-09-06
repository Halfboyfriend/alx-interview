#!/usr/bin/python3
"""
0. Prime Game
"""

def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def can_win(n):
        dp = [False] * (n + 1)
        dp[0] = False
        dp[1] = False

        for i in range(2, n + 1):
            if is_prime(i):
                dp[i] = True
            else:
                for j in range(2, i):
                    if i % j == 0 and dp[i - j] is False:
                        dp[i] = True
                        break

        return dp[n]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
