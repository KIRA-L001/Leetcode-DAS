"""
LeetCode 49. Group Anagrams (Medium)

Problem:
    Given an array of strings, group the anagrams together.

Approach:
    Anagrams share the same sorted character sequence. Use that sorted tuple
    as a hash-map key and collect words into buckets.

Complexity:
    Time:  O(n * k log k) - n words, each of length up to k, sorted.
    Space: O(n * k) - the buckets.
"""

from collections import defaultdict


def group_anagrams(strs):
    """Group words that are anagrams of each other."""
    buckets = defaultdict(list)
    for word in strs:
        buckets[tuple(sorted(word))].append(word)
    return list(buckets.values())


def _normalize(groups):
    """Sort groups and members so results compare deterministically."""
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    out = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert _normalize(out) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    print("All tests passed for 0049-group-anagrams")
