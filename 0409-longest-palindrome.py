"""
LeetCode 409. Longest Palindrome (Easy)

Problem:
    Given a string s of letters, return the length of the longest
    palindrome that can be built with those letters (case-sensitive).

Approach:
    Count characters. Every pair contributes 2. If any character has
    an odd count, one extra character can sit in the middle (+1).

Complexity:
    Time:  O(n)
    Space: O(1) — at most 52 distinct letters.
"""

from collections import Counter


def longest_palindrome(s):
    """Return the max length of a palindrome buildable from s."""
    length = 0
    has_odd = False
    for count in Counter(s).values():
        length += count // 2 * 2
        if count % 2:
            has_odd = True
    return length + 1 if has_odd else length


if __name__ == "__main__":
    assert longest_palindrome("abccccdd") == 7  # "dccaccd"
    assert longest_palindrome("a") == 1
    assert longest_palindrome("aa") == 2
    assert longest_palindrome("Aa") == 1  # case-sensitive
    assert longest_palindrome("ccc") == 3
    print("All tests passed for LeetCode 409.")
