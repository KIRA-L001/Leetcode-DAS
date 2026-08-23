from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict); dp = [True] + [False]*len(s)
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in words: dp[i] = True; break
        return dp[-1]

# refreshed 20260824-013656
