"""
LeetCode #37 - Sudoku Solver
Difficulty: Hard
"""
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(row, col, c):
            for i in range(9):
                if board[row][i] == c or board[i][col] == c:
                    return False
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == c:
                    return False
            return True

        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for c in '123456789':
                            if isValid(row, col, c):
                                board[row][col] = c
                                if solve():
                                    return True
                                board[row][col] = '.'
                        return False
            return True

        solve()
