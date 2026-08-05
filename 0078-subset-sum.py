"""
LeetCode #78 - Subsets
Difficulty: Medium
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(i, path):
            if i == len(nums):
                result.append(path[:])
                return
            backtrack(i + 1, path)
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
        backtrack(0, [])
        return result
