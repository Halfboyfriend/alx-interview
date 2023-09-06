#!/usr/bin/python3
"""
0. Prime Game
"""

def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def play_round(n):
        if n % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winner_count = {"Maria": 0, "Ben": 0}

    for i in range(x):
        n = nums[i]
        current_player = play_round(n)
        while n > 1:
            prime = 2
            if not is_prime(prime):
                prime += 1
            while n % prime != 0:
                prime += 2
                while not is_prime(prime):
                    prime += 2
            while n % prime == 0:
                n //= prime
            current_player = "Maria" if current_player == "Ben" else "Ben"

        winner_count[current_player] += 1

    if winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    elif winner_count["Ben"] > winner_count["Maria"]:
        return "Ben"
    else:
        return None
