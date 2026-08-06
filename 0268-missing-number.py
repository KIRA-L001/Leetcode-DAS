"""
LeetCode #268 - Missing Number
Difficulty: Easy
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)
