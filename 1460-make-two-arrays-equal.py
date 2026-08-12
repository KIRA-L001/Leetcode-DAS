"""
# 1460. Make Two Arrays Equal (Easy)
# You are given two integer arrays of the same length. The array arr is initially 
# equal to target array. In each operation, you can permute the array and then 
# reverse any subarray of arr.
# Return true if it's possible to make arr equal to target.

# NeetCode 150 / Blind 75: Array / Hash Map

Example 1:
    Input: target = [1,2,3,2,2], arr = [1,3,2,2,2]
    Output: true
    Explanation: 
        - Permute arr to [1,2,3,2,2]
        - Or we can achieve target through the allowed operations

Example 2:
    Input: target = [1,2,3], arr = [3,2,1]
    Output: true

Example 3:
    Input: target = [1,2], arr = [2,1]
    Output: true

Approach: Sorting
- Since we can permute and reverse subarrays, we can achieve any rearrangement
- Simply check if both arrays contain the same elements (same multiset)
- Sorting both and comparing is O(n log n)
- Or use Counter to compare element frequencies in O(n)

Time Complexity:  O(n log n) with sorting, O(n) with Counter
Space Complexity: O(n) for Counter
"""

from __future__ import annotations
from collections import Counter


def can_be_equal(target: list[int], arr: list[int]) -> bool:
    """Return true if arr can be transformed to target via permute and reverse operations."""
    return Counter(target) == Counter(arr)


# Sorting approach
def can_be_equal_sorted(target: list[int], arr: list[int]) -> bool:
    """Return true using sorting comparison."""
    return sorted(target) == sorted(arr)


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _test_can_be_equal():
    # Example 1
    assert can_be_equal([1, 2, 3, 2, 2], [1, 3, 2, 2, 2]) == True
    assert can_be_equal_sorted([1, 2, 3, 2, 2], [1, 3, 2, 2, 2]) == True
    
    # Example 2
    assert can_be_equal([1, 2, 3], [3, 2, 1]) == True
    assert can_be_equal_sorted([1, 2, 3], [3, 2, 1]) == True
    
    # Example 3
    assert can_be_equal([1, 2], [2, 1]) == True
    assert can_be_equal_sorted([1, 2], [2, 1]) == True
    
    # Not possible - different element counts
    assert can_be_equal([1, 2, 3], [1, 2, 2]) == False
    assert can_be_equal_sorted([1, 2, 3], [1, 2, 2]) == False
    
    # Same arrays
    assert can_be_equal([5, 5, 5], [5, 5, 5]) == True
    
    # Empty arrays
    assert can_be_equal([], []) == True
    
    # Single element
    assert can_be_equal([1], [1]) == True
    assert can_be_equal([1], [2]) == False
    
    # With zeros
    assert can_be_equal([0, 0, 1], [1, 0, 0]) == True
    
    # Different lengths (shouldn't happen per problem, but test anyway)
    assert can_be_equal([1, 2], [1, 2, 3]) == False
    
    print("All Make Two Arrays Equal tests passed!")


if __name__ == "__main__":
    _test_can_be_equal()