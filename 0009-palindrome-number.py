"""
LeetCode 0009 - Palindrome Number (Easy)

Return True if an integer reads the same backward, without strings.

Approach: reverse only the second half of the number and compare with
the remaining first half; stop when the halves meet.

Time:  O(log |x|)
Space: O(1)
"""


def is_palindrome(x: int) -> bool:
    # negatives and non-zero multiples of 10 can never be palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    half = 0
    while x > half:
        half = half * 10 + x % 10
        x //= 10
    # even length: x == half; odd length: middle digit is half % 10
    return x == half or x == half // 10


if __name__ == "__main__":
    assert is_palindrome(121) is True
    assert is_palindrome(-121) is False
    assert is_palindrome(10) is False
    assert is_palindrome(0) is True
    assert is_palindrome(1221) is True
    print("0009 OK")
