"""
LeetCode #12 - Integer to Roman
Difficulty: Medium
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = []
        for v, s in zip(vals, syms):
            while num >= v:
                result.append(s)
                num -= v
        return "".join(result)
