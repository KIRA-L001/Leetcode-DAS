"""
LeetCode 2535. Difference Between Element Sum and Digit Sum of an Array (Easy)

Problem:
    Given an integer array nums, return the difference between the sum of its
    elements (elementSum) and the sum of the digits of all its elements
    (digitSum). Formally, return elementSum - digitSum.

Approach:
    Compute the total of the elements, then compute the total of all decimal
    digits across all elements. The answer is their difference.

Complexity:
    Time:  O(n * d) where n = len(nums), d = avg number of digits.
    Space: O(1).
"""


def difference_of_sum(nums):
    """Return elementSum - digitSum for the given array."""
    element_sum = sum(nums)
    digit_sum = 0
    for num in nums:
        n = abs(num)
        while n:
            digit_sum += n % 10
            n //= 10
    return element_sum - digit_sum


if __name__ == "__main__":
    assert difference_of_sum([1, 15, 6, 3]) == 9
    assert difference_of_sum([1, 2, 3, 4]) == 0
    assert difference_of_sum([10, 20, 30]) == 54
    print("All tests passed for 2535-difference-between-element-sum-and-digit-sum-of-an-array")
