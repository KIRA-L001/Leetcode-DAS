"""
LeetCode 26. Remove Duplicates from Sorted Array (Easy)

Problem:
    Remove duplicates from a sorted array in-place so each unique element
    appears once. Return the number of unique elements k; the first k slots
    of the array must hold the unique values in order.

Approach:
    Two pointers: a slow "write" index for the next unique slot and a fast
    "read" index scanning the array. Copy a value forward only when it
    differs from the last written unique value.

Complexity:
    Time:  O(n) - single pass.
    Space: O(1) - in-place.
"""


def remove_duplicates(nums):
    """Deduplicate sorted nums in place; return the count of unique values."""
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


if __name__ == "__main__":
    a = [1, 1, 2]
    k = remove_duplicates(a)
    assert k == 2 and a[:k] == [1, 2]

    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(b)
    assert k == 5 and b[:k] == [0, 1, 2, 3, 4]

    c = []
    assert remove_duplicates(c) == 0

    d = [7]
    assert remove_duplicates(d) == 1 and d == [7]
    print("All tests passed for 0026-remove-duplicates-from-sorted-array")
