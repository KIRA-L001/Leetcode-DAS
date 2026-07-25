"""
LeetCode 15. 3Sum (Medium)

Problem:
    Given an integer array nums, return all unique triplets
    [nums[i], nums[j], nums[k]] such that they sum to zero.

Approach:
    Sort the array. Fix the first element, then use two pointers to find
    pairs summing to its negation. Skip duplicates at every position to keep
    the result set unique.

Complexity:
    Time:  O(n^2) - outer loop times linear two-pointer scan.
    Space: O(1) extra (ignoring the output and sort).
"""


def three_sum(nums):
    """Return all unique triplets in nums that sum to zero."""
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 2):
        if nums[i] > 0:
            break  # All remaining values are positive; no triplet possible.
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate anchors.
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates on both sides.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([]) == []
    print("All tests passed for 0015-3sum")
