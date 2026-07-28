"""
LeetCode 300. Longest Increasing Subsequence (Medium)

Problem:
    Given an integer array nums, return the length of the longest
    strictly increasing subsequence.

Approach:
    Patience sorting with binary search. Keep `tails`, where tails[i]
    is the smallest possible tail of an increasing subsequence of
    length i+1. For each x, binary-search its position and either
    extend `tails` or improve an existing tail.

Complexity:
    Time:  O(n log n)
    Space: O(n)
"""

from bisect import bisect_left


def length_of_lis(nums):
    """Return the length of the longest strictly increasing subsequence."""
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)      # extends the longest subsequence
        else:
            tails[i] = x         # smaller tail for length i+1
    return len(tails)


if __name__ == "__main__":
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4  # 2,3,7,101
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7]) == 1  # strictly increasing
    assert length_of_lis([1]) == 1
    assert length_of_lis([]) == 0
    print("All tests passed for LeetCode 300.")
