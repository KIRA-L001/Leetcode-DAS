"""
347. Top K Frequent Elements
Return the k most frequent elements in an array.

Approach: Count frequencies, use heapq.nlargest or Counter.most_common.
Time: O(n + k log n)  Space: O(n)
"""
from typing import List
from collections import Counter
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    cnt = Counter(nums)
    return heapq.nlargest(k, cnt.keys(), key=cnt.get)

if __name__ == "__main__":
    assert sorted(topKFrequent([1,1,1,2,2,3], 2)) == [1,2]
    assert topKFrequent([1], 1) == [1]
    print("0347 OK")