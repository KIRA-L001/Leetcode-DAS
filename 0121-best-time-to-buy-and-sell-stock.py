from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0; low = float('inf')
        for p in prices:
            low = min(low, p)
            best = max(best, p - low)
        return best

# refreshed 20260824-013656
