"""
LeetCode #53 - Maximum Subarray
Difficulty: Medium
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur = nums[0]
        for n in nums[1:]:
            cur = max(n, cur + n)
            max_sum = max(max_sum, cur)
        return max_sum
