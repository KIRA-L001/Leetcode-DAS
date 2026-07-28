"""
LeetCode 283. Move Zeroes (Easy)

Problem:
    Given an integer array nums, move all 0's to the end while keeping
    the relative order of the non-zero elements. Do it in-place.

Approach:
    Two pointers: `write` marks where the next non-zero belongs.
    Sweep with `read`; whenever nums[read] != 0 swap it into `write`.

Complexity:
    Time:  O(n)
    Space: O(1)
"""


def move_zeroes(nums):
    """Mutate nums in place, zeros pushed to the back."""
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
    return nums  # returned for testing convenience


if __name__ == "__main__":
    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeroes([0]) == [0]
    assert move_zeroes([1, 2, 3]) == [1, 2, 3]
    assert move_zeroes([0, 0, 1]) == [1, 0, 0]
    assert move_zeroes([]) == []
    print("All tests passed for LeetCode 283.")
