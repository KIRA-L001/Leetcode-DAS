"""
LeetCode 424. Longest Repeating Character Replacement (Medium)

Problem:
    Given a string s and integer k, you may replace at most k
    characters. Return the length of the longest substring containing
    a single repeated letter achievable after replacements.

Approach:
    Sliding window. Keep counts of letters inside the window and the
    count of the most frequent letter seen (max_freq). A window is
    valid while (window_size - max_freq) <= k; otherwise shrink from
    the left. max_freq never needs to decrease — the answer only
    improves when a higher frequency appears.

Complexity:
    Time:  O(n)
    Space: O(1) — 26 letter counts.
"""

from collections import defaultdict


def character_replacement(s, k):
    """Return the longest substring length after at most k replacements."""
    counts = defaultdict(int)
    left = 0
    max_freq = 0
    best = 0
    for right, ch in enumerate(s):
        counts[ch] += 1
        max_freq = max(max_freq, counts[ch])
        # Shrink until the window needs <= k replacements.
        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("AAAA", 0) == 4
    assert character_replacement("", 2) == 0
    assert character_replacement("ABCDE", 1) == 2
    print("All tests passed for LeetCode 424.")
