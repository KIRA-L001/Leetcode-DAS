"""
LeetCode #34 - Find First and Last Position of Element in Sorted Array
Difficulty: Medium
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l if l < len(nums) and nums[l] == target else -1
        def findRight():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return r if r >= 0 and nums[r] == target else -1
        return [findLeft(), findRight()]
