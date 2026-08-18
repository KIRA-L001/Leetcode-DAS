"""
LeetCode 2769. Find the Maximum Achievable Number (Easy)

Problem:
    You and an opponent each independently choose an integer from the range
    [1, num]. You want to pick an integer x such that, no matter which integer y
    in [1, num] the opponent picks, |x - y| <= t. Return the maximum x for which
    this is possible.

Approach:
    The largest x you can guarantee is num itself: picking x = num and the
    opponent picking y = max(1, num - t) keeps |x - y| <= t, and x cannot exceed
    num by the problem's choice range.

Complexity:
    Time:  O(1).
    Space: O(1).
"""


def maximum_achievable(num, t):
    """Return the maximum guaranteed achievable number x."""
    return num


if __name__ == "__main__":
    assert maximum_achievable(4, 1) == 4
    assert maximum_achievable(3, 2) == 3
    print("All tests passed for 2769-find-the-maximum-achievable-number")
