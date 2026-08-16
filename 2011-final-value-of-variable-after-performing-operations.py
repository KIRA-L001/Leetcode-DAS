"""
LeetCode 2011. Final Value of Variable After Performing Operations (Easy)

Problem:
    Given a list of strings operations of length n, each either "++X",
    "X++", "--X", or "X--". Initially X = 0 and each operation increments
    or decrements X by 1. Return the final value of X.

Approach:
    Count how many operations increment versus decrement. Every operation
    string contains either '+' (increment) or '-' (decrement), so we can
    decide purely from the presence of a '+' character.

Complexity:
    Time:  O(n) - scan each operation.
    Space: O(1).
"""


def final_value_after_operations(operations):
    """Return X after applying all increment/decrement operations."""
    x = 0
    for op in operations:
        if "+" in op:
            x += 1
        else:
            x -= 1
    return x


if __name__ == "__main__":
    assert final_value_after_operations(["--X", "X++", "X++"]) == 1
    assert final_value_after_operations(["++X", "++X", "X++"]) == 3
    assert final_value_after_operations(["X++", "++X", "--X", "X--"]) == 0
    print("All tests passed for 2011-final-value-of-variable-after-performing-operations")
