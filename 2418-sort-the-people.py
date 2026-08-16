"""
LeetCode 2418. Sort the People (Easy)

Problem:
    Given parallel arrays `names` and `heights`, return the names sorted by
    height in descending order.

Approach:
    Zip names with heights and sort by height descending.

Complexity:
    Time:  O(n log n).
    Space: O(n).
"""


def sort_people(names, heights):
    """Return names ordered by descending height."""
    return [n for n, _ in sorted(zip(names, heights), key=lambda p: p[1], reverse=True)]


if __name__ == "__main__":
    assert sort_people(["Mary", "John", "Emma"], [180, 165, 170]) == ["Mary", "Emma", "John"]
    assert sort_people(["Alice", "Bob", "Bob"], [155, 185, 150]) == ["Bob", "Alice", "Bob"]
    print("All tests passed for 2418-sort-the-people")
