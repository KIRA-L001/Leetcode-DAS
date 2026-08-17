"""
LeetCode 2570. Merge Two 2D Arrays by Summing Values (Easy)

Problem:
    Given two 2D arrays a and b where each element is [id, value], ids are
    unique within each array and both are sorted ascending by id. Merge them:
    for ids present in both, sum their values. Return the resulting array
    sorted by id ascending.

Approach:
    Accumulate values into a dictionary keyed by id, then emit sorted entries.

Complexity:
    Time:  O(n + m).
    Space: O(n + m).
"""


def merge_arrays(a, b):
    """Merge two id-value arrays summing equal ids."""
    totals = {}
    for arr in (a, b):
        for idx, val in arr:
            totals[idx] = totals.get(idx, 0) + val
    return [[k, totals[k]] for k in sorted(totals)]


if __name__ == "__main__":
    assert merge_arrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]) == [[1, 6], [2, 3], [3, 2], [4, 6]]
    assert merge_arrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]) == [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
    print("All tests passed for 2570-merge-two-2d-arrays-by-summing-values")
