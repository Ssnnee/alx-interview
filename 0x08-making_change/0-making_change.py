#!/usr/bin/python3
""" This module use the recusive to solve this problem """


def makeChange(coins, total, count=0):
    """Determine the fewest number of coins needed to meet a given amount"""
    if (total <= 0):
        return 0

    if not coins:
        return -1

    coins.sort(reverse=True)

    if (coins[0] > total):
        coins.pop(0)
        return makeChange(coins, total, count)
    else:
        reste = total - coins[0]
        count += 1
        if (reste == 0):
            return count
        else:
            return makeChange(coins, reste, count)
