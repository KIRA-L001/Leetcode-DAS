"""
LeetCode 1929. Concatenation of Array (Easy)

Problem:
    Given an integer array nums of length n, return the concatenation of
    nums + nums (length 2n, the array appended to itself).

Approach:
    Slice-and-add (or extend) to produce a new array of length 2n.

Complexity:
    Time:  O(n) - copying the elements.
    Space: O(n) - result array.
"""


def get_concatenation(nums):
    """Return nums concatenated with itself."""
    return nums + nums


if __name__ == "__main__":
    assert get_concatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert get_concatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
    assert get_concatenation([0]) == [0, 0]
    print("All tests passed for 1929-concatenation-of-array")
