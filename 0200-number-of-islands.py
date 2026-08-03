"""
Number of Islands (#200) — Medium — NeetCode 150 / Blind 75

Given an m x 2d grid of '1's (land) and '0's (water), return the number of
islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Time Complexity: O(m * n) — each cell visited at most once
Space Complexity: O(m * n) — recursion stack in worst case (full grid of 1s)

Examples:
    >>> num_islands([
    ...     ["1","1","1","1","0"],
    ...     ["1","1","0","1","0"],
    ...     ["1","1","0","0","0"],
    ...     ["0","0","0","0","0"],
    ... ])
    1
    >>> num_islands([
    ...     ["1","1","0","0","0"],
    ...     ["1","1","0","0","0"],
    ...     ["0","0","1","0","0"],
    ...     ["0","0","0","1","1"],
    ... ])
    3
    >>> num_islands([["0","0","0"],["0","0","0"]])
    0
    >>> num_islands([["1"]])
    1
"""

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """Count the number of islands using in-place DFS (flood fill).

    Modifies the grid in-place by marking visited land cells as '0' to
    avoid using extra space for a visited set.

    Args:
        grid: 2D list of '1' (land) and '0' (water) characters.

    Returns:
        The number of distinct islands.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int) -> None:
        """Flood-fill from (r, c), marking all connected land as water."""
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # mark as visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count


def num_islands_bfs(grid: List[List[str]]) -> int:
    """Count the number of islands using BFS with a queue.

    Avoids recursion depth limits for very large grids.

    Args:
        grid: 2D list of '1' (land) and '0' (water) characters.

    Returns:
        The number of distinct islands.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                grid[r][c] = '0'
                queue = [(r, c)]
                while queue:
                    cr, cc = queue.pop(0)
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'
                            queue.append((nr, nc))

    return count


# ─── Inline Tests ───────────────────────────────────────────────────────────

def _run_tests() -> None:
    """Run inline doctest-style assertions for both solutions."""
    # Example 1 — single island
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert num_islands([row[:] for row in grid1]) == 1
    assert num_islands_bfs([row[:] for row in grid1]) == 1

    # Example 2 — three islands
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands([row[:] for row in grid2]) == 3
    assert num_islands_bfs([row[:] for row in grid2]) == 3

    # Edge cases
    assert num_islands([["0", "0", "0"], ["0", "0", "0"]]) == 0
    assert num_islands([["1"]]) == 1
    assert num_islands([["0"]]) == 0
    assert num_islands([]) == 0
    assert num_islands([[]]) == 0

    # Single row / single column
    assert num_islands([["1", "0", "1", "0", "1"]]) == 3
    assert num_islands([["1"], ["0"], ["1"], ["1"]]) == 2

    # All land
    assert num_islands([["1", "1"], ["1", "1"]]) == 1

    # All water
    assert num_islands([["0", "0"], ["0", "0"]]) == 0

    print("All Number of Islands tests passed.")


if __name__ == "__main__":
    _run_tests()
