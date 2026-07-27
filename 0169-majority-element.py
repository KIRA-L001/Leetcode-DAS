"""
169. Majority Element
Given an array of size n, find the element that appears more than n/2 times (always exists).

Approach: Boyer-Moore voting — maintain a candidate and a count; cancel out mismatches.
Time: O(n)  Space: O(1).
"""
from typing import List

def majorityElement(nums: List[int]) -> int:
    cand, cnt = None, 0
    for x in nums:
        if cnt == 0:
            cand, cnt = x, 1
        else:
            cnt += 1 if x == cand else -1
    return cand

if __name__ == "__main__":
    assert majorityElement([3, 2, 3]) == 3
    assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majorityElement([1]) == 1
    print("0169 OK")
