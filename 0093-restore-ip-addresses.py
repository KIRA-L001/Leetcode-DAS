"""
LeetCode #93 - Restore IP Addresses
Difficulty: Medium
"""
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return
            for i in range(start + 1, min(start + 4, len(s)) + 1):
                segment = s[start:i]
                if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                backtrack(i, path + [segment])
        backtrack(0, [])
        return result
