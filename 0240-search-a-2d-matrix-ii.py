"""
240. Search a 2D Matrix II
Return True if target exists in an m x n matrix where rows are sorted left-to-right,
cols are sorted top-to-bottom.

Approach: Start top-right, move left if val > target, down if val < target. O(m+n).
Time: O(m+n)  Space: O(1)
"""
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    r, c = 0, len(matrix[0]) - 1
    while r < len(matrix) and c >= 0:
        if matrix[r][c] == target:
            return True
        if matrix[r][c] > target:
            c -= 1
        else:
            r += 1
    return False

if __name__ == "__main__":
    m = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[11,14,16,20,26]]
    assert searchMatrix(m, 5) is True
    assert searchMatrix(m, 20) is False
    print("0240 OK")