"""
LeetCode 2810. Faulty Keyboard (Easy)

Problem:
    A keyboard has a faulty 'i' key: whenever it is pressed, it deletes the
    character just before the cursor (a backspace). Given the final string s as
    typed, return the string that would actually be displayed.

Approach:
    Use a stack; on 'i' pop the last character, otherwise push.

Complexity:
    Time:  O(n).
    Space: O(n) for the stack.
"""


def final_string(s):
    """Return the displayed string after applying the faulty backspace 'i'."""
    result = []
    for ch in s:
        if ch == "i":
            if result:
                result.pop()
        else:
            result.append(ch)
    return "".join(result)


if __name__ == "__main__":
    assert final_string("string") == "stng"
    assert final_string("abc") == "abc"
    print("All tests passed for 2810-faulty-keyboard")
