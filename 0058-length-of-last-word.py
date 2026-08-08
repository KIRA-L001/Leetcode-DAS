"""
58. Length of Last Word (Easy)

Problem:
    Given a string s consisting of words and spaces, return the length of the
    last word in the string. A word is a maximal substring consisting of
    non-space characters only.

Approach:
    Traverse from the end of the string, skip trailing spaces, then count
    characters until we hit a space or the beginning of the string.

Complexity:
    Time:  O(n) - single pass from end to start.
    Space: O(1) - only a counter variable.
"""


def length_of_last_word(s):
    """Return the length of the last word in the string."""
    i = len(s) - 1
    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1
    
    length = 0
    # Count characters until space or beginning
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    
    return length


if __name__ == "__main__":
    assert length_of_last_word("Hello World") == 5
    assert length_of_last_word("   fly me   to   the moon  ") == 4
    assert length_of_last_word("luffy is still joyboy") == 6
    assert length_of_last_word("") == 0
    assert length_of_last_word("a") == 1
    
    print("All tests passed for 0058-length-of-last-word")