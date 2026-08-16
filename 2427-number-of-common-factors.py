"""
LeetCode 2427. Number of Common Factors (Easy)

Problem:
    Return the number of positive integers that evenly divide BOTH a and b.

Approach:
    Any common factor also divides gcd(a, b); count the divisors of the gcd.

Complexity:
    Time:  O(sqrt(min(a, b))).
    Space: O(1).
"""

import math


def common_factors(a, b):
    """Return how many positive integers divide both a and b."""
    g = math.gcd(a, b)
    count = 0
    i = 1
    while i * i <= g:
        if g % i == 0:
            count += 1
            if i != g // i:
                count += 1
        i += 1
    return count


if __name__ == "__main__":
    assert common_factors(12, 6) == 4
    assert common_factors(25, 30) == 2
    print("All tests passed for 2427-number-of-common-factors")
