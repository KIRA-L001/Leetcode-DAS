"""
LeetCode 392. Is Subsequence (Easy)

Problem:
    Given strings s and t, return True if s is a subsequence of t
    (s can be formed from t by deleting characters, order preserved).

Approach:
    Two pointers: advance through t; advance in s only when the
    characters match. s is a subsequence iff we consume all of s.

Complexity:
    Time:  O(len(t))
    Space: O(1)
"""


def is_subsequence(s, t):
    """Return True if s is a subsequence of t."""
    i = 0
    for ch in t:
        if i < len(s) and s[i] == ch:
            i += 1
    return i == len(s)


if __name__ == "__main__":
    assert is_subsequence("abc", "ahbgdc") is True
    assert is_subsequence("axc", "ahbgdc") is False
    assert is_subsequence("", "anything") is True
    assert is_subsequence("a", "") is False
    assert is_subsequence("", "") is True
    print("All tests passed for LeetCode 392.")
