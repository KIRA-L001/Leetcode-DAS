"""
# 1313. Decompress Run-Length Encoded List (Easy)
# Given a list of integers, where every pair of elements represents 
# [value, frequency], return the decompressed list.

# NeetCode 150 / Blind 75: Array

Example 1:
    Input: nums = [2,5,1,2,3,10]
    Output: [2,2,2,2,2,1,1,3,3,3,3,3,3,3,3,3,3]
    Explanation: 
        - First pair: [2, 5] -> [2, 2, 2, 2, 2]
        - Second pair: [1, 2] -> [1, 1]
        - Third pair: [3, 10] -> ten 3s

Example 2:
    Input: nums = [1,2,3,4]
    Output: [1,1,3,3,3,3]

Approach: Iterate by Pairs
- Read pairs (value, frequency) from the input
- Append value frequency times to result

Time Complexity:  O(n) — each pair processed once
Space Complexity: O(n) — output array size is sum of frequencies
"""

from __future__ import annotations


def decompress_rle(nums: list[int]) -> list[int]:
    """Decompress run-length encoded list where [value, freq] pairs repeat value freq times."""
    result = []
    
    for i in range(0, len(nums), 2):
        value = nums[i]
        freq = nums[i + 1]
        result.extend([value] * freq)
    
    return result


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _test_decompress_rle():
    # Example 1
    assert decompress_rle([2, 5, 1, 2, 3, 10]) == [
        2, 2, 2, 2, 2, 1, 1,
        *[3] * 10
    ]
    
    # Example 2
    assert decompress_rle([1, 2, 3, 4]) == [1, 1, 3, 3, 3, 3]
    
    # Single pair
    assert decompress_rle([5, 3]) == [5, 5, 5]
    
    # Zero frequency (edge case - should produce empty for that pair)
    assert decompress_rle([1, 0, 2, 3]) == [2, 2, 2]
    
    # Zero value
    assert decompress_rle([0, 5]) == [0, 0, 0, 0, 0]
    
    # Empty input
    assert decompress_rle([]) == []
    
    # Multiple pairs
    assert decompress_rle([1, 1, 2, 1, 3, 1]) == [1, 2, 3]
    
    # Large frequency
    assert decompress_rle([7, 0]) == []
    
    print("All Decompress Run-Length Encoded List tests passed!")


if __name__ == "__main__":
    _test_decompress_rle()