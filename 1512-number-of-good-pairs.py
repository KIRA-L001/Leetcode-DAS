"""
LeetCode 1512. Number of Good Pairs (Easy)

Problem:
    Given an array of integers nums, a pair (i, j) is "good" if
    nums[i] == nums[j] and i < j. Return the number of good pairs.

Approach:
    For each distinct value that appears c times, it contributes c*(c-1)/2
    good pairs (all unordered pairs among its indices). Tally counts with
    a Counter and sum the combinations.

Complexity:
    Time:  O(n) - single pass to count plus a pass over the counts.
    Space: O(k) - distinct values.
"""


def num_identical_pairs(nums):
    """Return the number of good (equal, ordered i<j) pairs in nums."""
    from collections import Counter
    counts = Counter(nums)
    return sum(c * (c - 1) // 2 for c in counts.values())


if __name__ == "__main__":
    assert num_identical_pairs([1, 2, 3, 1, 1, 3]) == 4
    assert num_identical_pairs([1, 1, 1, 1]) == 6
    assert num_identical_pairs([1, 2, 3]) == 0
    print("All tests passed for 1512-number-of-good-pairs")
