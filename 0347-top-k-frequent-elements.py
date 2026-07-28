"""
LeetCode 347. Top K Frequent Elements (Medium)

Problem:
    Given an integer array nums and an integer k, return the k most
    frequent elements (any order).

Approach:
    Bucket sort by frequency: count with a hash map, then place each
    value into bucket[count]. Walk buckets from high to low frequency
    collecting values until we have k.

Complexity:
    Time:  O(n) — counting + bucket walk.
    Space: O(n)
"""

from collections import Counter


def top_k_frequent(nums, k):
    """Return the k most frequent values in nums."""
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for value, freq in counts.items():
        buckets[freq].append(value)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for value in buckets[freq]:
            result.append(value)
            if len(result) == k:
                return result
    return result


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 5, 5, 6], 3)) == [4, 5, 6]
    print("All tests passed for LeetCode 347.")
