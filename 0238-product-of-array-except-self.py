from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums); out = [1]*n
        l = 1
        for i in range(n): out[i] = l; l *= nums[i]
        r = 1
        for i in range(n-1, -1, -1): out[i] *= r; r *= nums[i]
        return out

# refreshed 20260827-160255
