"""
LeetCode 0056 - Merge Intervals (Medium)

Merge all overlapping intervals.

Approach: sort by start; extend the last merged interval when the next
one overlaps it, otherwise start a new group.

Time:  O(n log n) for the sort
Space: O(n) for the output
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)  # overlap: extend
        else:
            merged.append([start, end])
    return merged


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert merge([[5, 6]]) == [[5, 6]]
    print("0056 OK")
