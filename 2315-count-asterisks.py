"""
LeetCode 2315. Count Asterisks (Easy)

Problem:
    A string contains zero or more pairs of '|' characters. Return the number
    of '*' characters that are NOT between any pair of '|'.

Approach:
    Walk the string tracking whether we are currently inside a '|' pair;
    count '*' only while outside a pair.

Complexity:
    Time:  O(n) - single pass.
    Space: O(1).
"""


def count_asterisks(s):
    """Count asterisks that are not enclosed by '|' pairs."""
    inside = False
    count = 0
    for ch in s:
        if ch == "|":
            inside = not inside
        elif ch == "*" and not inside:
            count += 1
    return count


if __name__ == "__main__":
    assert count_asterisks("l|*e*et|c**o|*de|") == 2
    assert count_asterisks("i|*am|*not|*sure") == 0
    print("All tests passed for 2315-count-asterisks")
