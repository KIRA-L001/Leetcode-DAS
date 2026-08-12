"""
LeetCode #60 - Permutation Sequence
Difficulty: Hard
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        nums = list(range(1, n + 1))
        k -= 1
        result = []
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            idx = k // fact
            k %= fact
            result.append(str(nums.pop(idx)))
        return "".join(result)
