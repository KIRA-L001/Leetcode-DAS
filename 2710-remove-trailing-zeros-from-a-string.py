"""
LeetCode 2710. Remove Trailing Zeros From a String (Easy)

Problem:
    Given a string num representing a non-negative integer, remove all trailing
    zeros and return the resulting string.

Approach:
    Strip trailing '0' characters.

Complexity:
    Time:  O(n).
    Space: O(1) extra (new string).
"""


def remove_trailing_zeros(num):
    """Return `num` with all trailing zeros removed."""
    return num.rstrip("0")


if __name__ == "__main__":
    assert remove_trailing_zeros("51230100") == "512301"
    assert remove_trailing_zeros("123") == "123"
    assert remove_trailing_zeros("0") == ""
    print("All tests passed for 2710-remove-trailing-zeros-from-a-string")
