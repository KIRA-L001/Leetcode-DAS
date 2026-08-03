"""
Valid Anagram (#242) — Easy — NeetCode 150 / Blind 75

Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

Time Complexity: O(n) — single pass over both strings
Space Complexity: O(1) — the counter holds at most 26 lowercase letters

Examples:
    >>> is_anagram("anagram", "nagaram")
    True
    >>> is_anagram("rat", "car")
    False
    >>> is_anagram("listen", "silent")
    True
    >>> is_anagram("", "")
    True
    >>> is_anagram("a", "ab")
    False
"""


def is_anagram(s: str, t: str) -> bool:
    """Check whether t is an anagram of s using a frequency counter.

    Args:
        s: The reference string.
        t: The string to check against s.

    Returns:
        True if t is an anagram of s, False otherwise.
    """
    if len(s) != len(t):
        return False

    freq = [0] * 26
    for ch_s, ch_t in zip(s, t):
        freq[ord(ch_s) - ord('a')] += 1
        freq[ord(ch_t) - ord('a')] -= 1

    return all(count == 0 for count in freq)


def is_anagram_sort(s: str, t: str) -> bool:
    """Check whether t is an anagram of s by sorting both strings.

    This is a simpler but less efficient approach — O(n log n) time.

    Args:
        s: The reference string.
        t: The string to check against s.

    Returns:
        True if t is an anagram of s, False otherwise.
    """
    return sorted(s) == sorted(t)


# ─── Inline Tests ───────────────────────────────────────────────────────────

def _run_tests() -> None:
    """Run inline doctest-style assertions for both solutions."""
    # Basic positive cases
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("listen", "silent") is True
    assert is_anagram("aacc", "ccac") is False

    # Edge cases
    assert is_anagram("", "") is True
    assert is_anagram("a", "a") is True
    assert is_anagram("a", "ab") is False
    assert is_anagram("ab", "a") is False

    # Same string
    assert is_anagram("abc", "abc") is True

    # Different lengths
    assert is_anagram("abc", "abcd") is False

    # Sort-based solution should match
    assert is_anagram_sort("anagram", "nagaram") is True
    assert is_anagram_sort("rat", "car") is False
    assert is_anagram_sort("listen", "silent") is True
    assert is_anagram_sort("", "") is True
    assert is_anagram_sort("a", "ab") is False

    print("All Valid Anagram tests passed.")


if __name__ == "__main__":
    _run_tests()
