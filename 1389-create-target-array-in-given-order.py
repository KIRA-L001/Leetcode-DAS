"""
# 1389. Create Target Array in the Given Order (Easy)
# Given two arrays of integers nums and index, create a target array by inserting 
# nums[i] at index[index[i]] in the target array. Start with an empty target array.

# NeetCode 150 / Blind 75: Array

Example 1:
    Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
    Output: [0,4,1,3,2]
    Explanation:
        - Insert 0 at index 0: [0]
        - Insert 1 at index 1: [0,1]
        - Insert 2 at index 2: [0,1,2]
        - Insert 3 at index 2: [0,1,3,2]
        - Insert 4 at index 1: [0,4,1,3,2]

Example 2:
    Input: nums = [1,2,3,4,5], index = [0,1,2,3,4]
    Output: [1,2,3,4,5]

Approach: Direct Simulation
- Use list.insert() to insert at the specified position
- Each insert shifts existing elements right

Time Complexity:  O(n^2) — each insert can take O(n) time
Space Complexity: O(n) — target array
"""

from __future__ import annotations


def create_target(nums: list[int], index: list[int]) -> list[int]:
    """Create target array by inserting nums[i] at index[i]."""
    target = []
    
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    
    return target


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _test_create_target():
    # Example 1
    assert create_target([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]) == [0, 4, 1, 3, 2]
    
    # Example 2
    assert create_target([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) == [1, 2, 3, 4, 5]
    
    # Empty arrays
    assert create_target([], []) == []
    
    # Single element
    assert create_target([5], [0]) == [5]
    
    # Insert at beginning each time
    assert create_target([1, 2, 3], [0, 0, 0]) == [3, 2, 1]
    
    # Insert at end each time
    assert create_target([1, 2, 3], [0, 1, 2]) == [1, 2, 3]
    
    # Mixed insertions
    assert create_target([1, 2, 3, 4], [0, 1, 1, 3]) == [1, 3, 2, 4]
    
    # All same index
    assert create_target([1, 1, 1], [0, 0, 0]) == [1, 1, 1]
    
    print("All Create Target Array in Given Order tests passed!")


if __name__ == "__main__":
    _test_create_target()