#!/usr/bin/python3
"""0-making_change.py"""


def makeChange(coins, total):
    """make change problem"""
    if total <= 0:
            return 0

    # Initialize dp array with a value larger than any possible number of coins
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
