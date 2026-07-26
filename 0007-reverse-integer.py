"""
LeetCode 0007 - Reverse Integer (Medium)

Reverse the digits of a signed 32-bit integer; return 0 on overflow.

Approach: pop digits with mod/div on the absolute value, rebuild the
number, then reapply the sign and check the 32-bit bounds.

Time:  O(log |x|)  (one pass over the digits)
Space: O(1)
"""


def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    n, rev = abs(x), 0
    while n:
        rev = rev * 10 + n % 10  # append last digit
        n //= 10
    rev *= sign
    return rev if -2**31 <= rev <= 2**31 - 1 else 0


if __name__ == "__main__":
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(120) == 21
    assert reverse(0) == 0
    assert reverse(1534236469) == 0  # overflows 32-bit on reversal
    print("0007 OK")
