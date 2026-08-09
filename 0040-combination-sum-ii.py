"""
LeetCode #40 - Combination Sum II
Difficulty: Medium
"""
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(i, path, total):
            if total == target:
                result.append(path[:])
                return
            if i >= len(candidates) or total > target:
                return
            path.append(candidates[i])
            dfs(i + 1, path, total + candidates[i])
            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, path, total)
        dfs(0, [], 0)
        return result
