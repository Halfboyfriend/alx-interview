#!/usr/bin/python3
"""
0. Prime Game
"""

def isWinner(x, nums):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def canWin(n):
        if n == 1:
            return False
        
        for i in range(2, n + 1):
            if isPrime(i):
                return True
        
        return False
    
    Ben = 0
    Maria = 0

    for j in nums:
        if canWin(j):
            if j % 2 == 0:
                Maria +=1
            else:
                Ben += 1
    
    if Maria > Ben:
        return 'Maria'
    elif Maria < Ben:
        return "Ben"
    else:
        return None
