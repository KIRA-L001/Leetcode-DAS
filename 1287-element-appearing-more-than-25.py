"""
# 1287. Element Appearing More Than 25% In Array (Easy)
# Given an integer array where all elements appear k times except one which appears 
# more than 25% of the time, return that element.

# NeetCode 150 / Blind 75: Array / Hash Map

Example 1:
    Input: arr = [1,2,2,6,6,6,6,7,10]
    Output: 6
    Explanation: 6 appears 4 times out of 10 elements (40% > 25%)

Example 2:
    Input: arr = [1,1]
    Output: 1

Approach: Hash Map or Boyer-Moore-like
- Since one element appears > 25%, we can count frequencies
- Or use the fact that any element appearing > 25% cannot be skipped
  by a majority voting approach for 25% threshold

Time Complexity:  O(n) — single pass
Space Complexity: O(n) — hash map stores counts (or O(1) with Boyer-Moore variant)
"""

from __future__ import annotations
from collections import Counter


def find_special_integer(arr: list[int]) -> int:
    """Return the element that appears more than 25% of the time."""
    n = len(arr)
    threshold = n // 4
    
    counts = Counter(arr)
    for num, count in counts.items():
        if count > threshold:
            return num
    
    # Should not reach here given problem constraints
    return arr[0]


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _test_find_special_integer():
    # Example 1
    assert find_special_integer([1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6
    
    # Example 2
    assert find_special_integer([1, 1]) == 1
    
    # All same elements
    assert find_special_integer([5, 5, 5, 5]) == 5
    
    # Element appears exactly 25% (threshold is > 25%)
    # For 4 elements, threshold is 1, so need count > 1
    assert find_special_integer([1, 2, 1, 2]) == 1  # 1 appears 2 times (50%)
    
    # Single element
    assert find_special_integer([42]) == 42
    
    # Element appears 50% of time
    assert find_special_integer([3, 3, 1, 2]) == 3
    
    # Long array
    assert find_special_integer([1, 1, 1, 1, 2, 3, 4]) == 1  # 1 appears 4/7 > 25%
    
    print("All Element Appearing More Than 25% tests passed!")


if __name__ == "__main__":
    _test_find_special_integer()