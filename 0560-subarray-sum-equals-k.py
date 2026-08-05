"""
# 560. Subarray Sum Equals K (Medium)
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# NeetCode 150 / Blind 75: Arrays / Hashing / Prefix Sum

Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2

Example 3:
    Input: nums = [1,-1,0], k = 0
    Output: 3

Approach: Prefix Sum + Hash Map
- Maintain a running cumulative sum as we iterate through the array.
- Use a hash map to count how many times each prefix sum has occurred.
- For each new prefix sum `curr`, check if `curr - k` has been seen before.
  If so, every occurrence of `curr - k` represents a subarray ending at the
  current index whose sum equals k.
- Initialize the map with {0: 1} to handle subarrays starting from index 0.

Time Complexity:  O(n) — single pass through the array
Space Complexity: O(n) — hash map stores up to n distinct prefix sums
"""

from __future__ import annotations


def subarray_sum(nums: list[int], k: int) -> int:
    """Return the number of contiguous subarrays whose sum equals k."""
    count = 0
    prefix_sum = 0
    # Map from prefix_sum value → number of times it has occurred
    prefix_count: dict[int, int] = {0: 1}

    for num in nums:
        prefix_sum += num
        # If (prefix_sum - k) exists, those are starting points of valid subarrays
        if prefix_sum - k in prefix_count:
            count += prefix_count[prefix_sum - k]
        # Record the current prefix sum
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _test_subarray_sum():
    # Example 1
    assert subarray_sum([1, 1, 1], 2) == 2

    # Example 2
    assert subarray_sum([1, 2, 3], 3) == 2

    # Example 3: subarrays [1,-1], [-1,0], [1,-1,0] all sum to 0
    assert subarray_sum([1, -1, 0], 0) == 3

    # Single element equal to k
    assert subarray_sum([5], 5) == 1

    # Single element not equal to k
    assert subarray_sum([5], 3) == 0

    # All zeros, k = 0 → every subarray counts: n*(n+1)/2
    assert subarray_sum([0, 0, 0, 0], 0) == 10  # 4+3+2+1

    # Negative numbers
    assert subarray_sum([1, -1, 1, -1, 1], 0) == 6

    # Large k not achievable
    assert subarray_sum([1, 2, 3], 100) == 0

    # Entire array sums to k
    assert subarray_sum([1, 2, 3, 4, 5], 15) == 1

    # Mixed positive and negative with multiple valid subarrays
    assert subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4

    # Empty array
    assert subarray_sum([], 0) == 0

    print("All Subarray Sum Equals K tests passed!")


if __name__ == "__main__":
    _test_subarray_sum()
