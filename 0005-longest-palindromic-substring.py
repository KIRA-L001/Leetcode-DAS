"""
LeetCode 5. Longest Palindromic Substring (Medium)

Problem:
    Given a string s, return the longest palindromic substring in s.

Approach:
    Expand around center. Every palindrome is centered at either a single
    character (odd length) or between two characters (even length). For each
    of the 2n - 1 centers, expand outward while the ends match and track the
    longest span found.

Complexity:
    Time:  O(n^2) - each expansion may scan up to n characters.
    Space: O(1) - only indices are stored.
"""


def longest_palindrome(s):
    """Return the longest palindromic substring of s."""
    if len(s) < 2:
        return s

    start, end = 0, 0

    def expand(left, right):
        """Expand around the center and return the palindrome bounds."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        for lo, hi in (expand(i, i), expand(i, i + 1)):
            if hi - lo > end - start:
                start, end = lo, hi

    return s[start:end + 1]


if __name__ == "__main__":
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") in ("a", "c")
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"
    print("All tests passed for 0005-longest-palindromic-substring")
