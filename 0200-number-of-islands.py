"""
200. Number of Islands
Given a 2D grid of '1' (land) and '0' (water), count the number of islands (connected 1s, 4-dir).

Approach: DFS flood-fill. For each unvisited '1', increment count and sink the whole island.
Time: O(rows*cols)  Space: O(rows*cols) recursion stack.
"""
from typing import List

def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count

if __name__ == "__main__":
    g = [list("11110"), list("11010"), list("11000"), list("00000")]
    assert numIslands(g) == 1
    g2 = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert numIslands(g2) == 3
    print("0200 OK")
