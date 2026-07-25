"""
3. Longest Substring Without Repeating Characters (Medium)

Problem:
    Given a string s, find the length of the longest substring without
    repeating characters.

Approach:
    Sliding window with a hash map of last-seen indices. Expand the right
    edge; when a repeat appears inside the window, jump the left edge past
    the previous occurrence.

Complexity:
    Time:  O(n) - each index visited once by the right pointer.
    Space: O(min(n, charset)) - map of last positions.
"""


def length_of_longest_substring(s):
    last_seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1  # skip past duplicate
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3  # "abc"
    assert length_of_longest_substring("bbbbb") == 1     # "b"
    assert length_of_longest_substring("pwwkew") == 3    # "wke"
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("au") == 2
    print("All tests passed for 0003-longest-substring")
