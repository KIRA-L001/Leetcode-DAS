from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left
        tail = []
        for n in nums:
            i = bisect_left(tail, n)
            if i == len(tail): tail.append(n)
            else: tail[i] = n
        return len(tail)

# refreshed 20260821-103019
