"""
LeetCode 2778. Sum of Squares of Special Elements (Easy)

Problem:
    Given a 1-indexed integer array nums, an element nums[i] is special if i is
    divisible by the number of divisors of nums[i]. Return the sum of the squares
    of all special elements.

Approach:
    Count divisors of each value and test the index divisibility, accumulating
    squares of special elements.

Complexity:
    Time:  O(n * sqrt(v)).
    Space: O(1).
"""


def sum_of_squares(nums):
    """Return the sum of squares of special elements in the 1-indexed array."""
    def divisor_count(x):
        count = 0
        for d in range(1, int(x ** 0.5) + 1):
            if x % d == 0:
                count += 1
                if d != x // d:
                    count += 1
        return count

    total = 0
    for i, x in enumerate(nums, start=1):
        if i % divisor_count(x) == 0:
            total += x * x
    return total


if __name__ == "__main__":
    assert sum_of_squares([1, 2, 3, 4]) == 5
    assert sum_of_squares([2, 3, 4, 5, 6]) == 50
    print("All tests passed for 2778-sum-of-squares-of-special-elements")
