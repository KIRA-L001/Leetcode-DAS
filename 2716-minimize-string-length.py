"""
LeetCode 2716. Minimize String Length (Easy)

Problem:
    Given a string s, you may remove any character as long as you keep at least
    one occurrence of each distinct character. Return the minimum possible
    length of the resulting string.

Approach:
    The minimum length equals the number of distinct characters in s.

Complexity:
    Time:  O(n).
    Space: O(n) for the set.
"""


def minimized_string_length(s):
    """Return the number of distinct characters in s."""
    return len(set(s))


if __name__ == "__main__":
    assert minimized_string_length("aaabc") == 3
    assert minimized_string_length("abaac") == 3
    assert minimized_string_length("cada") == 3
    print("All tests passed for 2716-minimize-string-length")
