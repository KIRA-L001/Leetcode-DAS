"""
LeetCode 2558. Take Gifts From the Richest Pile (Easy)

Problem:
    You are given an integer array gifts where gifts[i] is the number of gifts
    in the ith pile. Every second, you choose the pile with the maximum number
    of gifts, take all of them, and leave floor(sqrt(gifts[i])) gifts behind.
    Return the total number of gifts remaining after k seconds.

Approach:
    Use a max-heap (stored as negatives) to repeatedly pop the largest pile,
    reduce it to floor(sqrt(value)), and push it back, for k iterations. Then
    sum the remaining values.

Complexity:
    Time:  O((n + k) * log n).
    Space: O(n).
"""

import heapq
import math


def pick_gifts(gifts, k):
    """Return remaining gifts after k seconds of the richest-pile rule."""
    heap = [-g for g in gifts]
    heapq.heapify(heap)
    for _ in range(k):
        largest = -heapq.heappop(heap)
        heapq.heappush(heap, -int(math.isqrt(largest)))
    return -sum(heap)


if __name__ == "__main__":
    assert pick_gifts([25, 64, 9, 4, 100], 4) == 29
    assert pick_gifts([1, 2, 3], 1) == 4
    print("All tests passed for 2558-take-gifts-from-the-richest-pile")
