"""
LeetCode #76 - Minimum Window Substring
Difficulty: Hard
"""
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        lo = 0
        min_len, min_start = float('inf'), 0
        for hi, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            while missing == 0:
                if hi - lo + 1 < min_len:
                    min_len, min_start = hi - lo + 1, lo
                need[s[lo]] += 1
                if need[s[lo]] > 0:
                    missing += 1
                lo += 1
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]
