from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        return [x for x, _ in heapq.nlargest(k, c.items(), key=lambda kv: kv[1])]

# refreshed 20260821-102318
