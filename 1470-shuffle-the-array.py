"""
LeetCode 1470. Shuffle the Array (Easy)

Problem:
    Given an array nums of length 2n, where the first n elements and the
    last n elements are paired as (x1, y1, ..., xn, yn), return the array
    reshuffled as (x1, y1, x2, y2, ..., xn, yn).

Approach:
    Walk two pointers: one over the first half (i) and one over the second
    half (j = n + i), interleaving their values into a result list.

Complexity:
    Time:  O(n) - single pass.
    Space: O(n) - output array.
"""


def shuffle(nums, n):
    """Interleave the first and second halves of nums."""
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[n + i])
    return result


if __name__ == "__main__":
    assert shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
    assert shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]
    print("All tests passed for 1470-shuffle-the-array")
