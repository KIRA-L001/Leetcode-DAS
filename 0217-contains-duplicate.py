"""
217. Contains Duplicate
Given an integer array, return True if any value appears at least twice.

Approach: Set membership — insert while scanning; first repeat means True.
Time: O(n)  Space: O(n).
"""
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False

if __name__ == "__main__":
    assert containsDuplicate([1, 2, 3, 1]) is True
    assert containsDuplicate([1, 2, 3, 4]) is False
    assert containsDuplicate([]) is False
    print("0217 OK")
