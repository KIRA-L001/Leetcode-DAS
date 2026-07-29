"""
350. Intersection of Two Arrays II
Return the intersection with duplicates (count of each element = min(count1, count2)).

Approach: Use Counter, subtract counts, collect remaining.
Time: O(n+m)  Space: O(min(n,m))
"""
from typing import List
from collections import Counter

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    c1, c2 = Counter(nums1), Counter(nums2)
    res = []
    for x in c1:
        if x in c2:
            res.extend([x] * min(c1[x], c2[x]))
    return res

if __name__ == "__main__":
    assert sorted(intersect([1,2,2,1], [2,2])) == [2,2]
    assert sorted(intersect([4,9,5], [9,4,9,8,4])) == [4,9]
    print("0350 OK")