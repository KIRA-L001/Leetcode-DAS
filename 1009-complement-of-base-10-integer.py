"""
LeetCode 1009. Complement of Base 10 Integer (Easy)

Problem:
    The complement of an integer is the integer you get when you flip all
    the 0's to 1's and all the 1's to 0's in its binary representation.
    Return the complement of a non-negative integer n.

Approach:
    Build a bitmask of all 1's that has the same number of bits as n
    (the smallest power of two greater than n, minus one), then XOR n
    with that mask to flip every significant bit.

Complexity:
    Time:  O(1) - bounded by the number of bits (<= 32).
    Space: O(1).
"""


def bitwise_complement(n):
    """Return the bitwise complement of n in base 10."""
    if n == 0:
        return 1
    mask = 1
    while mask <= n:
        mask <<= 1
    return n ^ (mask - 1)


if __name__ == "__main__":
    assert bitwise_complement(5) == 2   # 101 -> 010
    assert bitwise_complement(7) == 0   # 111 -> 000
    assert bitwise_complement(10) == 5  # 1010 -> 0101
    assert bitwise_complement(0) == 1
    print("All tests passed for 1009-complement-of-base-10-integer")
