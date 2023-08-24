#!/usr/bin/python3

def makeChange(coins, total):
    # Make chanege
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3 (11 = 5 + 5 + 1)
