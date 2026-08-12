"""
# 1260. Shuffle the Array (Easy)
# Given an array of 2n integers in the form [x1, x2, ..., xn, y1, y2, ..., yn],
# return it in the form [x1, y1, x2, y2, ..., xn, yn].

# NeetCode 150 / Blind 75: Array

Example 1:
    Input: nums = [2,3,4,3,4,2], n = 3
    Output: [2,3,4,3,4,2]
    Explanation:
        The array is divided into two halves:
        - First half: [2, 3, 4]
        - Second half: [3, 4, 2]
        Shuffled: [2, 3, 2, 3, 4, 4]

Example 2:
    Input: nums = [2,3,5,4,1,7], n = 3
    Output: [2,5,3,4,1,7]

Approach: Direct Indexing
- For i from 0 to n-1:
  - result[2*i] = nums[i] (x values)
  - result[2*i+1] = nums[i+n] (y values)

Time Complexity:  O(n) — single pass through the array
Space Complexity: O(n) — new array of size 2n
"""

from __future__ import annotations


def shuffle(nums: list[int], n: int) -> list[int]:
    """Shuffle array where nums = [x1,x2,...,xn,y1,y2,...,yn] -> [x1,y1,x2,y2,...]."""
    result = []
    for i in range(n):
        result.append(nums[i])      # xi
        result.append(nums[i + n])  # yi
    return result


# Alternative in-place approach (more complex)
def shuffle_in_place(nums: list[int], n: int) -> list[int]:
    """In-place shuffle using encoding technique."""
    for i in range(n):
        # Encode both x and y at position i using 32-bit math
        nums[i] = (nums[i] << 32) | nums[i + n]
    
    for i in range(n):
        nums[2 * i] = nums[i] >> 32
        nums[2 * i + 1] = nums[i] & 0xFFFFFFFF
    
    return nums[:2 * n]


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _test_shuffle():
    # Example 1
    assert shuffle([2, 3, 4, 3, 4, 2], 3) == [2, 3, 4, 3, 4, 2]
    
    # Example 2
    assert shuffle([2, 3, 5, 4, 1, 7], 3) == [2, 5, 3, 4, 1, 7]
    
    # Single pair
    assert shuffle([1, 2], 1) == [1, 2]
    
    # Two pairs
    assert shuffle([1, 2, 3, 4], 2) == [1, 3, 2, 4]
    
    # All same values
    assert shuffle([5, 5, 5, 5], 2) == [5, 5, 5, 5]
    
    # With zeros
    assert shuffle([0, 1, 0, 1], 2) == [0, 0, 1, 1]
    
    # Test in-place version
    assert shuffle_in_place([2, 3, 4, 3, 4, 2], 3) == [2, 3, 4, 3, 4, 2]
    assert shuffle_in_place([2, 3, 5, 4, 1, 7], 3) == [2, 5, 3, 4, 1, 7]
    
    print("All Shuffle the Array tests passed!")


if __name__ == "__main__":
    _test_shuffle()