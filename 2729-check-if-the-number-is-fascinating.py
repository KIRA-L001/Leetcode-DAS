"""
LeetCode 2729. Check if The Number is Fascinating (Easy)

Problem:
    Given an integer n, concatenate n, 2*n, and 3*n. Return true if the
    resulting string contains every digit from 1 to 9 exactly once (and no
    zeros), otherwise false.

Approach:
    Build the concatenated string and verify it equals the sorted digits 1..9.

Complexity:
    Time:  O(d) where d is the number of digits.
    Space: O(d).
"""


def is_fascinating(n):
    """Return whether n, 2n, 3n together contain digits 1..9 exactly once."""
    concatenated = str(n) + str(2 * n) + str(3 * n)
    return "0" not in concatenated and sorted(concatenated) == [str(d) for d in range(1, 10)]


if __name__ == "__main__":
    assert is_fascinating(192) is True
    assert is_fascinating(100) is False
    print("All tests passed for 2729-check-if-the-number-is-fascinating")
