"""
LeetCode 2744. Find Maximum Number of String Pairs (Easy)

Problem:
    You are given a 0-indexed array of distinct strings words, each of length 2.
    A pair (i, j) is valid if words[i] + words[j] is a palindrome, which for
    length-2 strings means words[j] is the reverse of words[i]. Return the
    maximum number of such pairs you can form (each string used at most once).

Approach:
    Greedily match each word with its reverse using a seen set.

Complexity:
    Time:  O(n).
    Space: O(n) for the set.
"""


def maximum_number_of_string_pairs(words):
    """Return the maximum number of reversible word pairs."""
    seen = set()
    pairs = 0
    for w in words:
        rev = w[::-1]
        if rev in seen:
            pairs += 1
            seen.discard(rev)
        else:
            seen.add(w)
    return pairs


if __name__ == "__main__":
    assert maximum_number_of_string_pairs(["ab", "ba", "abc", "cba"]) == 2
    assert maximum_number_of_string_pairs(["aabb", "abab"]) == 0
    print("All tests passed for 2744-find-maximum-number-of-string-pairs")
