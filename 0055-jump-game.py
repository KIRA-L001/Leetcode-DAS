"""
LeetCode #55 - Jump Game
Difficulty: Medium
NeetCode 150 / Blind 75

You are given a non-negative integer array nums. You are initially positioned
at the first index (index 0), and each element nums[i] represents the maximum
jump length from that position.

Return true if you can reach the last index, or false otherwise.

Approach: Greedy — track the furthest reachable index
- Start with goal = last index.
- Iterate from the end of the array backwards.
- At each position i, if i + nums[i] >= goal, then position i can reach the goal,
  so update goal = i.
- At the end, if goal == 0, we can reach the last index from the start.

Alternative: Forward greedy
- Track the furthest index we can reach so far (max_reach).
- At each index i, if i > max_reach, we can't proceed further → return False.
- Update max_reach = max(max_reach, i + nums[i]).
- If max_reach >= last index, return True.

Time Complexity: O(n) single pass through the array.
Space Complexity: O(1) only a few variables.
"""


def can_jump(nums: list[int]) -> bool:
    """Return True if you can reach the last index of the array.

    Uses a greedy approach tracking the furthest reachable index.

    >>> can_jump([2, 3, 1, 1, 4])
    True
    >>> # Start at index 0 (jump up to 2), jump to index 1 (jump up to 3),
    >>> # jump to index 4 (last index).

    >>> can_jump([3, 2, 1, 0, 4])
    False
    >>> # You will always arrive at index 3 (value 0), which blocks further progress.

    >>> can_jump([0])
    True
    >>> # Already at the last index.

    >>> can_jump([1])
    True
    >>> # Single element, already at the last index.

    >>> can_jump([1, 0])
    True
    >>> # Jump from index 0 to index 1 (last index).

    >>> can_jump([0, 1])
    False
    >>> # Stuck at index 0, can't move forward.

    >>> can_jump([2, 0, 0])
    True
    >>> # Jump from index 0 directly to index 2 (last index).

    >>> can_jump([1, 1, 1, 1])
    True
    >>> # Step forward one at a time.

    >>> can_jump([5, 0, 0, 0, 0, 0])
    True
    >>> # Jump from index 0 all the way to the end.
    """
    max_reach = 0
    n = len(nums)

    for i in range(n):
        # If current index is beyond what we can reach, we're stuck
        if i > max_reach:
            return False
        # Update the furthest index we can reach
        max_reach = max(max_reach, i + nums[i])
        # Early exit: if we can already reach or pass the last index
        if max_reach >= n - 1:
            return True

    return True


def can_jump_backward(nums: list[int]) -> bool:
    """Alternative backward-greedy approach.

    Start from the last index and work backwards. If position i can reach
    the current goal, update the goal to i. If goal reaches 0, return True.

    >>> can_jump_backward([2, 3, 1, 1, 4])
    True
    >>> can_jump_backward([3, 2, 1, 0, 4])
    False
    >>> can_jump_backward([0])
    True
    >>> can_jump_backward([1, 0])
    True
    >>> can_jump_backward([0, 1])
    False
    """
    n = len(nums)
    goal = n - 1  # the last index we want to reach

    for i in range(n - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    # Additional manual tests
    print("\n--- Manual Tests ---")

    # Test 1: Classic true case
    assert can_jump([2, 3, 1, 1, 4]) is True, "Test 1 failed"
    print("Test 1 passed: [2,3,1,1,4] → True")

    # Test 2: Classic false case
    assert can_jump([3, 2, 1, 0, 4]) is False, "Test 2 failed"
    print("Test 2 passed: [3,2,1,0,4] → False")

    # Test 3: Single element
    assert can_jump([0]) is True, "Test 3 failed"
    print("Test 3 passed: [0] → True")

    # Test 4: Single element (non-zero)
    assert can_jump([5]) is True, "Test 4 failed"
    print("Test 4 passed: [5] → True")

    # Test 5: Two elements, can jump
    assert can_jump([1, 0]) is True, "Test 5 failed"
    print("Test 5 passed: [1,0] → True")

    # Test 6: Two elements, stuck
    assert can_jump([0, 1]) is False, "Test 6 failed"
    print("Test 6 passed: [0,1] → False")

    # Test 7: Stuck at index 1 (can't reach end)
    assert can_jump([1, 0, 0, 0]) is False, "Test 7 failed"
    print("Test 7 passed: [1,0,0,0] → False")

    # Test 8: All zeros except first (can't reach end)
    assert can_jump([0, 0, 0, 0]) is False, "Test 8 failed"
    print("Test 8 passed: [0,0,0,0] → False")

    # Test 9: Large array
    assert can_jump([1] * 10000) is True, "Test 9 failed"
    print("Test 9 passed: Large array of 1s → True")

    # Test 10: Large array with trap
    nums = [1] * 9999 + [0]
    assert can_jump(nums) is True, "Test 10 failed"
    print("Test 10 passed: Large array with zero at end → True")

    # Test 11: Trap in the middle
    nums = [1, 1, 0, 1]
    assert can_jump(nums) is False, "Test 11 failed"
    print("Test 11 passed: Trap in middle → False")

    # Test 12: Backward approach matches forward
    assert can_jump([2, 3, 1, 1, 4]) == can_jump_backward([2, 3, 1, 1, 4])
    assert can_jump([3, 2, 1, 0, 4]) == can_jump_backward([3, 2, 1, 0, 4])
    print("Test 12 passed: Forward and backward approaches agree")

    print("\nAll tests passed!")
