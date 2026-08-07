
"""
LeetCode #16 - 3Sum Closest
Difficulty: Medium
"""
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = float('inf')
        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if abs(s - target) < abs(best - target):
                    best = s
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
                else:
                    return s
        return best
