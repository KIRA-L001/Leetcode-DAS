from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0]); dp = [0]*(n+1); best = 0
        for i in range(m):
            prev = 0
            for j in range(1, n+1):
                tmp = dp[j]
                if matrix[i][j-1] == '1':
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    best = max(best, dp[j])
                else: dp[j] = 0
                prev = tmp
        return best * best

# refreshed 20260905-100059
