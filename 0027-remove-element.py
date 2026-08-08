"""
27. Remove Element (Easy)

Problem:
    Given an integer array nums and an integer val, remove all occurrences
    of val in nums in-place. The order of elements may be changed. Return
    the number of elements in nums that are not equal to val.

Approach:
    Two-pointer technique. Use a write pointer to track where to place
    non-val elements. Iterate through the array and copy non-val elements
    to the write position, incrementing write when a non-val element is found.

Complexity:
    Time:  O(n) - single pass through the array.
    Space: O(1) - in-place modification with only two variables.
"""


def remove_element(nums, val):
    """Remove all occurrences of val from nums in-place.
    
    Returns the count of elements not equal to val.
    """
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1
    return write


if __name__ == "__main__":
    # Test 1
    nums1 = [3, 2, 2, 3]
    k1 = remove_element(nums1, 3)
    assert k1 == 2, f"Expected 2, got {k1}"
    assert nums1[:k1] == [2, 2], f"Expected [2, 2], got {nums1[:k1]}"
    
    # Test 2
    nums2 = [0, 1, 2, 2, 1, 0]
    k2 = remove_element(nums2, 0)
    assert k2 == 4, f"Expected 4, got {k2}"
    assert nums2[:k2] == [1, 2, 2, 1], f"Expected [1, 2, 2, 1], got {nums2[:k2]}"
    
    print("All tests passed for 0027-remove-element")