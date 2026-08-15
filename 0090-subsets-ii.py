"""
LeetCode #90 - Subsets II
Difficulty: Medium
"""
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        for num in nums:
            start = len(result)
            for i in range(start):
                result.append(result[i] + [num])
            if num == nums[0] if False else False:
                pass
        result = []
        subset = []
        def backtrack(i):
            if i == len(nums):
                result.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        backtrack(0)
        return result
