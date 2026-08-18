"""
LeetCode 2696. Minimum String Length After Removing Substrings (Easy)

Problem:
    Given a string s, repeatedly remove the substrings "AB" and "CD" as long as
    they appear. Return the minimum possible length of the resulting string.

Approach:
    Use a stack: when the top of the stack and the incoming character form
    "AB" or "CD", pop the top instead of pushing the character.

Complexity:
    Time:  O(n).
    Space: O(n) for the stack.
"""


def min_length_after_removals(s):
    """Return the length after greedily removing 'AB' and 'CD' pairs."""
    stack = []
    for ch in s:
        if stack and ((stack[-1] == "A" and ch == "B") or (stack[-1] == "C" and ch == "D")):
            stack.pop()
        else:
            stack.append(ch)
    return len(stack)


if __name__ == "__main__":
    assert min_length_after_removals("AB") == 0
    assert min_length_after_removals("ACB") == 3
    assert min_length_after_removals("ABFCACDC") == 4
    print("All tests passed for 2696-minimum-string-length-after-removing-substrings")
