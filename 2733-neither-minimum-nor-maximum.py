"""
LeetCode 2733. Neither Minimum nor Maximum (Easy)

Problem:
    Given an integer array nums, return an element of nums that is neither the
    minimum nor the maximum value. If no such element exists, return -1.

Approach:
    Scan for any value different from the global min and max.

Complexity:
    Time:  O(n).
    Space: O(1).
"""


def find_non_min_or_max(nums):
    """Return an element that is neither min nor max, or -1 if none exists."""
    if len(nums) <= 2:
        return -1
    mn, mx = min(nums), max(nums)
    for x in nums:
        if x != mn and x != mx:
            return x
    return -1


if __name__ == "__main__":
    assert find_non_min_or_max([3, 2, 1, 4]) in (2, 3)
    assert find_non_min_or_max([1, 2]) == -1
    print("All tests passed for 2733-neither-minimum-nor-maximum")
