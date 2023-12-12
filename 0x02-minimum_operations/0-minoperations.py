#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    count1, count2 = 0, 2
    while count2 <= n:
        # if n evenly divides by count2
        if n % count2 == 0:
            # total even-divisions by count2 = total operations
            count1 += count2
            # set n to the remainder
            n = n / count2
            # reduce count2 to find remaining smaller vals that evenly-divide n
            count2 -= 1
        # increment count2 until it evenly-divides n
        count2 += 1
    return count1
