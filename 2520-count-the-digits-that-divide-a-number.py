"""
LeetCode 2520. Count the Digits That Divide a Number (Easy)

Problem:
    Given an integer num, count how many of its digits divide num evenly.

Approach:
    Extract each decimal digit; if non-zero and num % digit == 0, count it.

Complexity:
    Time:  O(number of digits).
    Space: O(1).
"""


def count_digits(num):
    """Count digits of num that divide num without remainder."""
    n = num
    count = 0
    while n:
        d = n % 10
        if d != 0 and num % d == 0:
            count += 1
        n //= 10
    return count


if __name__ == "__main__":
    assert count_digits(7) == 1
    assert count_digits(121) == 2
    assert count_digits(1248) == 4
    print("All tests passed for 2520-count-the-digits-that-divide-a-number")
