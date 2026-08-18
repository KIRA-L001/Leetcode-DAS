"""
LeetCode 2828. Check if a String is a Prefix of an Array (Easy)

Problem:
    Given an array of strings words and a string s, return true if s is a prefix
    of the concatenation of some prefix of words (i.e. joining words from the
    start yields exactly s, or a prefix of s once we reach its length).

Approach:
    Concatenate words left-to-right until the joined length reaches len(s), then
    compare.

Complexity:
    Time:  O(total characters).
    Space: O(total characters) for the joined prefix.
"""


def is_prefix_string(s, words):
    """Return whether concatenating a prefix of words equals s."""
    joined = ""
    for w in words:
        joined += w
        if len(joined) >= len(s):
            break
    return joined == s


if __name__ == "__main__":
    assert is_prefix_string("iloveleetcode", ["i", "love", "leetcode", "apples"]) is True
    assert is_prefix_string("iloveleetcode", ["apples", "i"]) is False
    print("All tests passed for 2828-check-if-a-string-is-a-prefix-of-an-array")
