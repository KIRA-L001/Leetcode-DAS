"""
LeetCode 11. Container With Most Water (Medium)

Problem:
    Given n vertical lines of given heights, find two lines that together
    with the x-axis form a container holding the most water.

Approach:
    Two pointers from both ends. The area is limited by the shorter line, so
    moving the shorter pointer inward is the only way the area can improve.

Complexity:
    Time:  O(n) - each pointer moves at most n steps.
    Space: O(1).
"""


def max_area(height):
    """Return the maximum water area between two lines."""
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        best = max(best, width * min(height[left], height[right]))
        # Advance the pointer at the shorter line.
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    print("All tests passed for 0011-container-with-most-water")
