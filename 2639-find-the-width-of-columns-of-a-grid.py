"""
LeetCode 2639. Find the Width of Columns of a Grid (Easy)

Problem:
    You are given a 0-indexed m x n grid of strings. Return an array of length n
    where the ith element is the width of the ith column, defined as the maximum
    string length among all cells in that column.

Approach:
    Walk each column and take the maximum length per column.

Complexity:
    Time:  O(m * n).
    Space: O(n) for the answer.
"""


def find_column_width(grid):
    """Return the maximum width of each column."""
    if not grid:
        return []
    n = len(grid[0])
    widths = [0] * n
    for row in grid:
        for j, cell in enumerate(row):
            widths[j] = max(widths[j], len(str(cell)))
    return widths


if __name__ == "__main__":
    assert find_column_width([["1", "22", "333"], ["4444", "5", "66"]]) == [4, 2, 3]
    assert find_column_width([["a"], ["bb"], ["ccc"]]) == [3]
    print("All tests passed for 2639-find-the-width-of-columns-of-a-grid")
