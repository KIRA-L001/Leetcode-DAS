"""
LeetCode #53 - Maximum Subarray
Difficulty: Medium
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = cur = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num)
            best = max(best, cur)
        return best
