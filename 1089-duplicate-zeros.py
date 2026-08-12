"""
# 1089. Duplicate Zeros (Easy)
# Given an integer array arr, write a function that duplicates each occurrence 
# of zero, shifting the remaining elements to the right.
# Elements beyond the end of the array are not written.
# The array is modified in-place.

# NeetCode 150 / Blind 75: Array

Example 1:
    Input: arr = [1,0,2,3,0,4,5,0]
    Output: [1,0,0,2,3,0,0,4]
    Explanation: 
        - Duplicate the 0 at index 1, shift elements right
        - Duplicate the 0 at index 5, shift elements right
        - The final 0 at index 7 is not written

Example 2:
    Input: arr = [1,2,3]
    Output: [1,2,3]

Approach: Two-Pass
- First pass: count how many elements will be written
- Second pass: iterate from right and place elements
- This avoids shifting elements multiple times

Time Complexity:  O(n) — two passes through the array
Space Complexity: O(1) — modifies in-place
"""

from __future__ import annotations


def duplicate_zeros(arr: list[int]) -> None:
    """Modify arr in-place, duplicating each zero and shifting right."""
    n = len(arr)
    
    # First pass: find the length of the new array
    i = 0
    length = 0
    while length < n:
        if arr[i] == 0:
            length += 2
        else:
            length += 1
        i += 1
    
    # Adjust i to be within bounds
    i -= 1
    if length > n:
        arr[n - 1] = 0
        n -= 1
    
    # Second pass: write from the end
    while n > 0:
        if arr[i] == 0:
            arr[n - 1] = 0
            arr[n - 2] = 0
            n -= 2
        else:
            arr[n - 1] = arr[i]
            n -= 1
        i -= 1


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _test_duplicate_zeros():
    # Example 1
    arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_zeros(arr1)
    assert arr1 == [1, 0, 0, 2, 3, 0, 0, 4]
    
    # Example 2
    arr2 = [1, 2, 3]
    duplicate_zeros(arr2)
    assert arr2 == [1, 2, 3]
    
    # Leading zeros
    arr3 = [0, 0, 0]
    duplicate_zeros(arr3)
    assert arr3 == [0, 0, 0]
    
    # Single element, non-zero
    arr4 = [5]
    duplicate_zeros(arr4)
    assert arr4 == [5]
    
    # Single element, zero (only first zero written)
    arr5 = [0]
    duplicate_zeros(arr5)
    assert arr5 == [0]
    
    # All zeros
    arr6 = [0, 0, 0, 0]
    duplicate_zeros(arr6)
    assert arr6 == [0, 0, 0, 0]
    
    # No zeros
    arr7 = [1, 2, 3, 4, 5]
    duplicate_zeros(arr7)
    assert arr7 == [1, 2, 3, 4, 5]
    
    # Trailing zero
    arr8 = [8, 4, 1, 0]
    duplicate_zeros(arr8)
    assert arr8 == [8, 4, 1, 1]
    
    print("All Duplicate Zeros tests passed!")


if __name__ == "__main__":
    _test_duplicate_zeros()