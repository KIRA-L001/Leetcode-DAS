
"""
LeetCode #29 - Divide Two Integers
Difficulty: Medium
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        result = 0
        for shift in range(31, -1, -1):
            if (a >> shift) >= b:
                a -= b << shift
                result += 1 << shift
        result = -result if neg else result
        return min(max(result, -2**31), 2**31 - 1)
