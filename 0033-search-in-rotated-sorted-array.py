"""
LeetCode 33. Search in Rotated Sorted Array (Medium)

Problem:
    A sorted array of distinct integers is rotated at an unknown pivot.
    Find the index of a target value, or -1 if absent, in O(log n) time.

Approach:
    Modified binary search. At each step at least one half of the range is
    properly sorted; check whether the target lies inside that sorted half
    and narrow the search accordingly.

Complexity:
    Time:  O(log n).
    Space: O(1).
"""


def search(nums, target):
    """Return index of target in rotated sorted nums, or -1."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:  # Left half is sorted.
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted.
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert search([5, 1, 3], 5) == 0
    print("All tests passed for 0033-search-in-rotated-sorted-array")
