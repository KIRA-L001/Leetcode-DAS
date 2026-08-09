"""
LeetCode #42 - Trapping Rain Water
Difficulty: Hard
"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        lo, hi, left_max, right_max, water = 0, len(height) - 1, 0, 0, 0
        while lo < hi:
            if height[lo] < height[hi]:
                if height[lo] >= left_max:
                    left_max = height[lo]
                else:
                    water += left_max - height[lo]
                lo += 1
            else:
                if height[hi] >= right_max:
                    right_max = height[hi]
                else:
                    water += right_max - height[hi]
                hi -= 1
        return water
