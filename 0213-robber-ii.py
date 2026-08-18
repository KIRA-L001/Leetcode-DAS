from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return nums[0] if nums else 0
        def helper(a):
            prev = cur = 0
            for n in a:
                prev, cur = cur, max(cur, prev + n)
            return cur
        return max(helper(nums[:-1]), helper(nums[1:]))
