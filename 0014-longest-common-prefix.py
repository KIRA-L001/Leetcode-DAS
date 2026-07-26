"""
LeetCode 0014 - Longest Common Prefix (Easy)

Find the longest common prefix among a list of strings.

Approach: compare characters column by column (vertical scanning);
stop at the first mismatch or when the shortest string ends.

Time:  O(S) where S is the total number of characters
Space: O(1)
"""


def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    for i, ch in enumerate(strs[0]):
        for other in strs[1:]:
            if i >= len(other) or other[i] != ch:
                return strs[0][:i]
    return strs[0]


if __name__ == "__main__":
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix(["single"]) == "single"
    assert longest_common_prefix(["ab", "a"]) == "a"
    print("0014 OK")
