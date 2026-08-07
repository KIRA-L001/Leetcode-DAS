
"""
LeetCode #17 - Letter Combinations of a Phone Number
Difficulty: Medium
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        def dfs(i, path):
            if i == len(digits):
                result.append("".join(path))
                return
            for c in phone[digits[i]]:
                path.append(c)
                dfs(i + 1, path)
                path.pop()
        dfs(0, [])
        return result
