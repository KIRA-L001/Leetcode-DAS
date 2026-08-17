"""
LeetCode 2574. Left and Right Sum Differences (Easy)

Problem:
    Given a 0-indexed integer array nums, for each index i compute
    leftSum[i] = sum(nums[:i]) (0 if i == 0) and rightSum[i] = sum(nums[i+1:])
    (0 if i == last). Return an array of abs(leftSum[i] - rightSum[i]).

Approach:
    Build prefix and suffix running sums, then take absolute differences.

Complexity:
    Time:  O(n).
    Space: O(n).
"""


def left_right_difference(nums):
    """Return abs(leftSum - rightSum) for every index."""
    n = len(nums)
    left = 0
    right = sum(nums)
    result = []
    for x in nums:
        right -= x
        result.append(abs(left - right))
        left += x
    return result


if __name__ == "__main__":
    assert left_right_difference([10, 4, 8, 3]) == [15, 1, 11, 22]
    assert left_right_difference([1]) == [0]
    print("All tests passed for 2574-left-and-right-sum-differences")
