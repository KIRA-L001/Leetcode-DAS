from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        m, n = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O': return
            board[r][c] = 'S'
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]: dfs(r+dr, c+dc)
        for r in range(m):
            dfs(r, 0); dfs(r, n-1)
        for c in range(n):
            dfs(0, c); dfs(m-1, c)
        for r in range(m):
            for c in range(n):
                board[r][c] = 'X' if board[r][c] == 'O' else board[r][c]
                if board[r][c] == 'S': board[r][c] = 'O'
