"""
LeetCode 70. Climbing Stairs (Easy)

Problem:
    You climb a staircase of n steps taking 1 or 2 steps at a time.
    How many distinct ways can you reach the top?

Approach:
    Classic Fibonacci recurrence: ways(n) = ways(n - 1) + ways(n - 2).
    Iterate bottom-up keeping only the last two values.

Complexity:
    Time:  O(n).
    Space: O(1).
"""


def climb_stairs(n):
    """Return the number of distinct ways to climb n steps."""
    prev, curr = 1, 1  # ways(0), ways(1)
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89
    assert climb_stairs(45) == 1836311903
    print("All tests passed for 0070-climbing-stairs")
