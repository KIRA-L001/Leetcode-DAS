"""
LeetCode 416. Partition Equal Subset Sum (Medium)

Problem:
    Given an array nums, return True if it can be split into two
    subsets with equal sums.

Approach:
    0/1 knapsack on target = total // 2. dp is a bitset-like boolean
    array where dp[j] means "some subset sums to j". Iterate items,
    updating j from high to low so each item is used at most once.

Complexity:
    Time:  O(n * target)
    Space: O(target)
"""


def can_partition(nums):
    """Return True if nums can be partitioned into two equal-sum subsets."""
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
        if dp[target]:
            return True
    return dp[target]


if __name__ == "__main__":
    assert can_partition([1, 5, 11, 5]) is True   # {1,5,5} and {11}
    assert can_partition([1, 2, 3, 5]) is False
    assert can_partition([2, 2]) is True
    assert can_partition([1]) is False
    assert can_partition([100, 100, 100, 100]) is True
    print("All tests passed for LeetCode 416.")
