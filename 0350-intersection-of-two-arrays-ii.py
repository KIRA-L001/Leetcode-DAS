from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums1); out = []
        for n in nums2:
            if c.get(n, 0) > 0: out.append(n); c[n] -= 1
        return out

# refreshed 20260918-100000
