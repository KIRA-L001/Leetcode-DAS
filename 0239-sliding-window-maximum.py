"""
239. Sliding Window Maximum
You are given an array of integers and a window size k. Return the max for each sliding window.

Approach: Monotonic deque — maintain decreasing order, front is max, pop smaller from back.
Time: O(n)  Space: O(k)
"""
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    from collections import deque
    dq = deque()
    res = []
    for i, x in enumerate(nums):
        while dq and dq[0][0] <= i - k:
            dq.popleft()
        while dq and dq[-1][1] <= x:
            dq.pop()
        dq.append((i, x))
        if i >= k - 1:
            res.append(dq[0][1])
    return res

if __name__ == "__main__":
    assert maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert maxSlidingWindow([1], 1) == [1]
    print("0239 OK")