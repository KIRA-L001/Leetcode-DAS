"""
LeetCode 2553. Separate the Digits in an Array (Easy)

Problem:
    Given an array of positive integers nums, return an array of the digits of
    each integer in the order they appear.

Approach:
    For each number, peel off digits (most-significant first to preserve order)
    and append them to the result.

Complexity:
    Time:  O(n * d).
    Space: O(n * d) for the output.
"""


def separate_digits(nums):
    """Return the list of digits of all numbers, in order."""
    result = []
    for num in nums:
        digits = []
        n = num
        while n:
            digits.append(n % 10)
            n //= 10
        result.extend(reversed(digits))
    return result


if __name__ == "__main__":
    assert separate_digits([13, 25, 83, 77]) == [1, 3, 2, 5, 8, 3, 7, 7]
    assert separate_digits([7, 1, 4]) == [7, 1, 4]
    assert separate_digits([100, 2]) == [1, 0, 0, 2]
    print("All tests passed for 2553-separate-the-digits-in-an-array")
