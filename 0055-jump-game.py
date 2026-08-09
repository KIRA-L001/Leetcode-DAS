"""
LeetCode #55 - Jump Game
Difficulty: Medium
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, num in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + num)
        return True
