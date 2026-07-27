"""
167. Two Sum II - Input Array Is Sorted
Given a 1-indexed sorted array, find two indices (1-based) that sum to target. Exactly one answer.

Approach: Two pointers (lo at start, hi at end). Move lo up if sum too small, hi down if too big.
Time: O(n)  Space: O(1).
"""
from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        s = numbers[lo] + numbers[hi]
        if s == target:
            return [lo + 1, hi + 1]
        if s < target:
            lo += 1
        else:
            hi -= 1
    return []

if __name__ == "__main__":
    assert twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert twoSum([2, 3, 4], 6) == [1, 3]
    assert twoSum([-1, 0], -1) == [1, 2]
    print("0167 OK")
