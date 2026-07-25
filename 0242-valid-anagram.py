"""
242. Valid Anagram (Easy)

Problem:
    Given two strings s and t, return True if t is an anagram of s.

Approach:
    Count character frequencies of both strings and compare. A single
    counter incremented for s and decremented for t works in one pass each.

Complexity:
    Time:  O(n)
    Space: O(k) where k is alphabet size.
"""

from collections import Counter


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    counts = Counter(s)
    counts.subtract(t)
    return all(v == 0 for v in counts.values())


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    print("All tests passed for 0242-valid-anagram")
