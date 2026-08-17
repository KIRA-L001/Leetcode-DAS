"""
LeetCode 2652. Sum Multiples (Easy)

Problem:
    Given two integers n and a 3-element array of distinct positive integers,
    return the sum of all integers in the range [1, n] that are divisible by at
    least one element of the array.

Approach:
    Iterate 1..n and accumulate numbers divisible by any of the divisors.

Complexity:
    Time:  O(n).
    Space: O(1).
"""


def sum_of_multiples(n, divisors):
    """Return the sum of numbers in [1, n] divisible by any divisor."""
    total = 0
    for i in range(1, n + 1):
        if any(i % d == 0 for d in divisors):
            total += i
    return total


if __name__ == "__main__":
    assert sum_of_multiples(7, [2, 3]) == 15
    assert sum_of_multiples(10, [3, 5]) == 33
    print("All tests passed for 2652-sum-multiples")
