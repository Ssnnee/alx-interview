#!/usr/bin/python3

def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given amount"""
    if total <= 0:
        return 0
    if len(coins) == 0:
        return 0
    if total < coins[0]:
        return makeChange(coins[1:], total)
    return makeChange(coins, total - coins[0]) + makeChange(coins[1:], total)
