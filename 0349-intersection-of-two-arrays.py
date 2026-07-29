"""
349. Intersection of Two Arrays
Return the intersection of two arrays (distinct values only).

Approach: Use a set for nums1, then collect matches from nums2.
Time: O(n+m)  Space: O(min(n,m))
"""
from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    s = set(nums1)
    res = set()
    for x in nums2:
        if x in s:
            res.add(x)
    return list(res)

if __name__ == "__main__":
    assert sorted(intersection([1,2,2,1], [2,2])) == [2]
    assert sorted(intersection([4,9,5], [9,4,9,8,4])) == [4,9]
    print("0349 OK")