"""
1. Two Sum (Easy)

Problem:
    Given an array of integers `nums` and an integer `target`, return the
    indices of the two numbers that add up to `target`. Exactly one solution
    exists and an element may not be used twice.

Approach:
    Single pass with a hash map storing value -> index. For each number,
    check if (target - number) was already seen; if so, we have our pair.

Complexity:
    Time:  O(n) - one pass over the array.
    Space: O(n) - hash map of seen values.
"""


def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # per constraints this is never reached


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All tests passed for 0001-two-sum")
