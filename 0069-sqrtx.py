"""
69. Sqrt(x) (Easy)

Problem:
    Given a non-negative integer x, return the square root of x rounded down
    to the nearest integer. The returned integer is also known as the
    floor of the square root of x.

Approach:
    Binary search between 1 and x. Find the largest mid where mid * mid <= x.
    When the search ends, right will be the floor of the square root.

Complexity:
    Time:  O(log x) - binary search halves search space.
    Space: O(1) - only two pointer variables.
"""


def my_sqrt(x):
    """Return the floor of the square root of x."""
    if x < 2:
        return x
    
    left, right = 1, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right


if __name__ == "__main__":
    assert my_sqrt(4) == 2
    assert my_sqrt(9) == 3
    assert my_sqrt(0) == 0
    assert my_sqrt(1) == 1
    assert my_sqrt(8) == 2
    
    print("All tests passed for 0069-sqrtx")