class Solution:
    def trailingZeroes(self, n: int) -> int:
        z = 0
        while n: n //= 5; z += n
        return z

# refreshed 20261110-100020
