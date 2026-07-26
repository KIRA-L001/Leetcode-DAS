"""
LeetCode 0066 - Plus One (Easy)

Increment a large integer represented as an array of digits.

Approach: walk from the least significant digit, propagating the carry;
a digit < 9 absorbs the carry and we can return early.

Time:  O(n)
Space: O(1) extra (O(n) only when all digits are 9)
"""


def plus_one(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # 9 rolls over, carry continues
    return [1] + digits  # all nines: 999 -> 1000


if __name__ == "__main__":
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plus_one([9]) == [1, 0]
    assert plus_one([9, 9, 9]) == [1, 0, 0, 0]
    print("0066 OK")
