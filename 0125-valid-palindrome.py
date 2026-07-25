"""
LeetCode 125. Valid Palindrome (Easy)

Problem:
    Return True if a string is a palindrome considering only alphanumeric
    characters and ignoring case.

Approach:
    Two pointers from both ends. Skip non-alphanumeric characters, compare
    lowercased characters, and move inward until the pointers cross.

Complexity:
    Time:  O(n) - each character examined at most once per pointer.
    Space: O(1) - no extra copy of the string.
"""


def is_palindrome(s):
    """Return True if s is a palindrome over its alphanumeric characters."""
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
    assert is_palindrome("ab_a") is True
    print("All tests passed for 0125-valid-palindrome")
