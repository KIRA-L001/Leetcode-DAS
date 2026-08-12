"""
LeetCode #84 - Largest Rectangle in Histogram
Difficulty: Hard
"""
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, best = [], 0
        for i, h in enumerate(heights + [0]):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                best = max(best, height * width)
            stack.append(i)
        return best
