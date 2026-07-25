"""
53. Maximum Subarray (Medium)

Problem:
    Given an integer array nums, find the contiguous subarray with the
    largest sum and return that sum.

Approach:
    Kadane's algorithm: keep a running sum of the best subarray ending at
    the current index; restart the sum when it would drag the total down.

Complexity:
    Time:  O(n)
    Space: O(1)
"""


def max_sub_array(nums):
    best = current = nums[0]
    for n in nums[1:]:
        # either extend the previous subarray or start fresh at n
        current = max(n, current + n)
        best = max(best, current)
    return best


if __name__ == "__main__":
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # [4,-1,2,1]
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
    assert max_sub_array([-3, -1, -2]) == -1
    print("All tests passed for 0053-maximum-subarray")
