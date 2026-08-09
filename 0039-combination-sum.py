"""
LeetCode #39 - Combination Sum
Difficulty: Medium
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, path, total):
            if total == target:
                result.append(path[:])
                return
            if i >= len(candidates) or total > target:
                return
            path.append(candidates[i])
            dfs(i, path, total + candidates[i])
            path.pop()
            dfs(i + 1, path, total)
        dfs(0, [], 0)
        return result
