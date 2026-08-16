"""
LeetCode 2235. Add Two Integers (Easy)

Problem:
    Given two integers num1 and num2, return their sum.

Approach:
    Trivial arithmetic addition. Included for completeness of the easy
    track; the real value is exercising the self-contained test harness.

Complexity:
    Time:  O(1).
    Space: O(1).
"""


def sum(num1, num2):
    """Return the sum of two integers."""
    return num1 + num2


if __name__ == "__main__":
    assert sum(12, 5) == 17
    assert sum(-10, 4) == -6
    assert sum(0, 0) == 0
    print("All tests passed for 2235-add-two-integers")
