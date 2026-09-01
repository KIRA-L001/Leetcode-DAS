from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = cnt = 0
        for n in nums:
            if cnt == 0: cand = n
            cnt += 1 if n == cand else -1
        return cand

# refreshed 20260901-114103
