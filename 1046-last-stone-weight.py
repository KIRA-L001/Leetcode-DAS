"""
# 1046. Last Stone Weight (Easy)
# You are given an array of integers stones where stones[i] is the weight of the i-th stone.
# If two stones have equal weight, they both destroy each other.
# Otherwise, the lighter stone is destroyed and the heavier stone gains the difference.
# Return the weight of the surviving stone, or 0 if no stones remain.

# NeetCode 150 / Blind 75: Heap / Priority Queue

Example 1:
    Input: stones = [2,7,4,1,8,1]
    Output: 1
    Explanation: 
        - First combine 2 and 1 to get 1, stones = [7,4,1,8,1]
        - Combine 7 and 8 to get 1, stones = [4,1,1,1]
        - Combine 4 and 1 to get 3, stones = [1,3]
        - Combine 1 and 3 to get 2, stones = [2]
        - Surviving stone weighs 1

Example 2:
    Input: stones = [1]
    Output: 1

Approach: Max Heap
- Use a max heap (simulated with negative values in Python's min-heap)
- Always pop the two heaviest stones
- If they differ, push the difference back
- Continue until 0 or 1 stones remain

Time Complexity:  O(n log n) — each heap operation is O(log n)
Space Complexity: O(n) — heap stores all stones
"""

import heapq
from __future__ import annotations


def last_stone_weight(stones: list[int]) -> int:
    """Return the weight of the last surviving stone, or 0 if none remain."""
    # Max heap using negative values
    heap = [-s for s in stones]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        y = -heapq.heappop(heap)  # Heaviest
        x = -heapq.heappop(heap)  # Second heaviest
        
        if y > x:
            heapq.heappush(heap, -(y - x))
    
    return -heap[0] if heap else 0


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _test_last_stone_weight():
    # Example 1
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1
    
    # Example 2
    assert last_stone_weight([1]) == 1
    
    # All same weight - all destroyed
    assert last_stone_weight([3, 3, 3, 3]) == 0
    
    # Single pair
    assert last_stone_weight([5, 3]) == 2
    
    # Empty list
    assert last_stone_weight([]) == 0
    
    # All same weight except one
    assert last_stone_weight([1, 1, 1]) == 1
    
    # Large difference
    assert last_stone_weight([100, 1]) == 99
    
    # Two equal stones
    assert last_stone_weight([5, 5]) == 0
    
    print("All Last Stone Weight tests passed!")


if __name__ == "__main__":
    _test_last_stone_weight()