"""
20. Valid Parentheses (Easy)

Problem:
    Given a string containing only '()[]{}', determine if the input is
    valid: brackets must be closed by the same type and in the right order.

Approach:
    Use a stack. Push opening brackets; on a closing bracket, the stack top
    must be its matching opener, otherwise the string is invalid. The string
    is valid iff the stack is empty at the end.

Complexity:
    Time:  O(n) - each character processed once.
    Space: O(n) - stack in the worst case (all openers).
"""


def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            # closing bracket must match most recent opener
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("(") is False
    print("All tests passed for 0020-valid-parentheses")
