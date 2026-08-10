"""
LeetCode #51 - N-Queens
Difficulty: Hard
"""
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols, diag1, diag2 = set(), set(), set()

        def backtrack(row, board):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or row + col in diag1 or row - col in diag2:
                    continue
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                backtrack(row + 1, board)
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, board)
        return result
