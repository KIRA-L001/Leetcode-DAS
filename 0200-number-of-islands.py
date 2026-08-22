from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0]); cnt = 0
        def dfs(r, c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c] != '1': return
            grid[r][c] = '0'
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]: dfs(r+dr, c+dc)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1': cnt += 1; dfs(r, c)
        return cnt

# refreshed 20260822-140033
