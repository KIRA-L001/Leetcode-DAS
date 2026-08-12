"""
LeetCode #85 - Maximal Rectangle
Difficulty: Hard
"""
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        best = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            best = max(best, self._largest(heights))
        return best

    def _largest(self, heights):
        stack, best = [], 0
        for i, h in enumerate(heights + [0]):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                best = max(best, height * width)
            stack.append(i)
        return best
