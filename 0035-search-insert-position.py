"""
35. Search Insert Position (Easy)

Problem:
    Given a sorted array of distinct integers and a target value, return
    the index if the target is found. If not, return the index where it
    would be if it were inserted in order.

Approach:
    Binary search to find the insertion position. Track left and right
    pointers. When the loop ends, left is the correct insertion position
    since it represents the first element greater than or equal to target.

Complexity:
    Time:  O(log n) - binary search halves the search space each iteration.
    Space: O(1) - only two pointer variables used.
"""


def search_insert(nums, target):
    """Find the index to insert target in a sorted array.
    
    Returns the index of target if found, otherwise the insertion position.
    """
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    assert search_insert([], 5) == 0
    
    print("All tests passed for 0035-search-insert-position")