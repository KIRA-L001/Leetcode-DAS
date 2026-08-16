"""
LeetCode 1920. Build Array from Permutation (Easy)

Problem:
    Given a zero-based permutation nums (each integer 0..n-1 appears once),
    build an array ans of the same length where ans[i] = nums[nums[i]].
    Return ans.

Approach:
    Compute each entry directly from the definition; no extra constraint
    beyond O(n) time and O(1) extra space (the output array is allowed).

Complexity:
    Time:  O(n) - one pass.
    Space: O(n) - output array.
"""


def build_array(nums):
    """Return ans where ans[i] = nums[nums[i]]."""
    return [nums[nums[i]] for i in range(len(nums))]


if __name__ == "__main__":
    assert build_array([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]
    assert build_array([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]
    print("All tests passed for 1920-build-array-from-permutation")
