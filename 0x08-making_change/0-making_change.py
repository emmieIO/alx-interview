#!/usr/bin/python3
"""0-making_change.py"""


def makeChange(coins, total):
    """make change problem"""
    coins.sort()
    dp = [0] * (total + 1)

    for i in range(1, total+1):
        minn = float("inf")

        for coin in coins:
            diff = i - coin
            if diff < 0:
                break
            min(minn, dp[diff] + 1)
        dp[i] = minn

        if dp[total] < float('inf'):
            return dp[total]
        else:
            return -1
