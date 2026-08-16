"""
LeetCode 1480. Running Sum of 1d Array (Easy)

Problem:
    Given an array nums, return its running sum where running_sum[i] is the
    sum of nums[0] + nums[1] + ... + nums[i].

Approach:
    Iterate left to right, maintaining a running total and appending it to
    the result as we go (in-place variant also possible).

Complexity:
    Time:  O(n) - single pass.
    Space: O(n) - output array.
"""


def running_sum(nums):
    """Return the prefix sums of nums."""
    result = []
    total = 0
    for x in nums:
        total += x
        result.append(total)
    return result


if __name__ == "__main__":
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert running_sum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    print("All tests passed for 1480-running-sum-of-1d-array")
